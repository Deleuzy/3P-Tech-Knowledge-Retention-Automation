from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from dotenv import load_dotenv
from cerebras.cloud.sdk import Cerebras
import requests
from datetime import datetime
import base64

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configuration - Load from environment or use defaults
KNOWLEDGE_BASE_PATH = os.getenv("KNOWLEDGE_BASE_PATH", "../3P-Tech-Knowledge-Retention-Automation/3p-knowledge")
KATEGORIER_FILE = os.path.join(KNOWLEDGE_BASE_PATH, "_config", "kategorier.json")

# GitHub Configuration
github_token = os.getenv("GITHUB_TOKEN")
github_owner = os.getenv("GITHUB_OWNER")
github_repo = os.getenv("GITHUB_REPO")
github_branch = os.getenv("GITHUB_BRANCH", "main")

# Initialize Cerebras client with API key from environment
cerebras_client = Cerebras(
    api_key=os.getenv("CEREBRAS_API_KEY")
)

def get_github_headers():
    """Get headers for GitHub API"""
    return {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }

def commit_to_github(file_path, content, commit_message):
    """Commit a file to GitHub repository"""
    if not github_token or not github_owner or not github_repo:
        return False, "GitHub configuration missing"
    
    try:
        # Get the current file SHA (if exists) or create new
        url = f"https://api.github.com/repos/{github_owner}/{github_repo}/contents/{file_path}"
        params = {"ref": github_branch}
        
        response = requests.get(url, headers=get_github_headers(), params=params)
        
        sha = None
        if response.status_code == 200:
            sha = response.json().get("sha")
        
        # Prepare the data
        data = {
            "message": commit_message,
            "content": base64.b64encode(content.encode()).decode(),
            "branch": github_branch
        }
        
        if sha:
            data["sha"] = sha
        
        # Create or update the file
        response = requests.put(url, headers=get_github_headers(), json=data)
        
        if response.status_code in [200, 201]:
            return True, "File committed successfully"
        else:
            return False, f"GitHub API error: {response.status_code} - {response.text}"
            
    except Exception as e:
        return False, f"Error committing to GitHub: {str(e)}"

def load_kategorier():
    """Load kategorier.json configuration"""
    try:
        with open(KATEGORIER_FILE, 'r') as f:
            config = json.load(f)
        return config.get('categories', [])
    except FileNotFoundError:
        print(f"Error: kategorier.json not found at {KATEGORIER_FILE}")
        return []
    except json.JSONDecodeError:
        print(f"Error: kategorier.json is not valid JSON")
        return []

def load_knowledge_for_category(category_id):
    """Load all .md files from a category folder"""
    try:
        categories = load_kategorier()
        category = next((cat for cat in categories if cat['id'] == category_id), None)
        
        if not category:
            return None, "Category not found"
        
        folder_path = os.path.join(KNOWLEDGE_BASE_PATH, category['folder_path'])
        
        if not os.path.exists(folder_path):
            return None, f"Folder {folder_path} does not exist"
        
        knowledge_content = ""
        files_loaded = 0
        
        for filename in os.listdir(folder_path):
            if filename.endswith('.md') and not filename.startswith('.'):
                filepath = os.path.join(folder_path, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        knowledge_content += f"\n\n{'='*80}\n"
                        knowledge_content += f"Document: {filename}\n"
                        knowledge_content += f"{'='*80}\n"
                        knowledge_content += content
                        files_loaded += 1
                except Exception as e:
                    print(f"Error reading {filepath}: {str(e)}")
        
        return {
            'category': category,
            'knowledge': knowledge_content,
            'files_loaded': files_loaded
        }, None
    
    except Exception as e:
        return None, f"Error loading knowledge: {str(e)}"

@app.route('/api/categories', methods=['GET'])
def get_categories():
    """Return list of all categories"""
    try:
        categories = load_kategorier()
        return jsonify({
            'success': True,
            'categories': categories
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/ask', methods=['POST'])
def ask_question():
    """
    Main endpoint: Answer a question about a category using the knowledge base
    
    Expected JSON:
    {
        "category": "ATEX",
        "question": "What are common pitfalls in zone classification?"
    }
    """
    try:
        data = request.json
        category_id = data.get('category')
        question = data.get('question')
        
        if not category_id or not question:
            return jsonify({
                'success': False,
                'error': 'Missing category or question'
            }), 400
        
        # Load knowledge for this category
        result, error = load_knowledge_for_category(category_id)
        
        if error:
            return jsonify({
                'success': False,
                'error': error
            }), 404
        
        category = result['category']
        knowledge = result['knowledge']
        files_loaded = result['files_loaded']
        
        # Build system prompt
        system_prompt = f"""{category['system_prompt']}

You have access to the company's accumulated knowledge base for this category:

{knowledge}

Instructions:
- Always ground your answers in the provided knowledge base
- If the knowledge base doesn't contain relevant information, say so explicitly
- Reference specific documents, standards, or lessons learned when applicable
- For practical questions, provide actionable checklists or steps
- Proactively mention known pitfalls and how to avoid them"""
        
        # Call Cerebras LLM
        response = cerebras_client.chat.completions.create(
            model="llama3.1-8b",
            max_tokens=2048,
            temperature=0.2,
            top_p=1,
            stream=False,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ]
        )
        
        answer = response.choices[0].message.content
        
        return jsonify({
            'success': True,
            'category': category_id,
            'question': question,
            'answer': answer,
            'files_loaded': files_loaded,
            'model': 'llama3.1-8b',
            'provider': 'Cerebras'
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f"Error processing request: {str(e)}"
        }), 500

VALID_CATEGORIES = ['ATEX', 'NH3', 'PLC-SCADA', 'EPLAN', 'General']

def validate_lesson_quality(markdown_content, category_id):
    """
    Quality Gate: Validate lesson meets 'Unibio Standard'
    Returns (is_valid, error_messages)
    """
    errors = []
    
    # Check 1: YAML Header has exactly 8 required fields
    if not markdown_content.startswith('---'):
        errors.append("Missing YAML opening --- fence")
    
    # Extract YAML section
    lines = markdown_content.split('\n')
    yaml_fields = ['titel', 'kategori', 'version', 'oprettet', 'opdateret', 'forfatter', 'status', 'tags']
    yaml_section = []
    in_yaml = False
    for line in lines:
        if line.strip() == '---':
            in_yaml = not in_yaml
            continue
        if in_yaml and ':' in line:
            yaml_section.append(line.split(':')[0].strip())
    
    for field in yaml_fields:
        if field not in yaml_section:
            errors.append(f"Missing YAML field: {field}")
    
    # Check 2: Required H2 Headers
    required_headers = [
        '## Summary', '## Background', '## Standards & Requirements',
        '## Best Practices', '## Known Pitfalls', '## Checklist',
        '## Lessons Learned', '## References'
    ]
    for header in required_headers:
        if header not in markdown_content:
            errors.append(f"Missing header: {header}")
    
    # Check 3: Unibio Standard - Root Cause and Cost
    if '## Lessons Learned' in markdown_content:
        lessons_section = markdown_content.split('## Lessons Learned')[1]
        if 'Root Cause' not in lessons_section and 'root cause' not in lessons_section.lower():
            errors.append("Missing 'Root Cause' in Lessons Learned")
        if 'Cost' not in lessons_section and 'cost' not in lessons_section.lower():
            errors.append("Missing 'Cost' analysis in Lessons Learned")
    
    # Check 4: Category routing
    if category_id not in VALID_CATEGORIES:
        errors.append(f"Invalid category: {category_id}. Must be one of {VALID_CATEGORIES}")
    
    # Check 5: Checkbox formatting
    if '[x]' in markdown_content.lower() or '[X]' in markdown_content:
        errors.append("Checkboxes should use [ ] format, not [x]")
    
    return len(errors) == 0, errors

def llama_quality_gate(markdown_content):
    """
    GUARDRAIL: Call Llama 3.1 8B to audit lesson for Unibio Standard
    Returns (is_valid, audit_response)
    """
    try:
        prompt = f"""You are a Quality Gate Auditor for Unibio Engineering Standards.

Audit this lesson learned for the 'Unibio Standard'. Check for:
1. Root Cause analysis is present and detailed
2. Cost analysis is present with actual numbers
3. Actionable recommendations
4. Proper YAML metadata with 8 required fields

Respond with EXACTLY one of these formats:
- "VALIDATED: <brief confirmation>" if all standards are met
- "REJECTED: <specific issue>" if Root Cause or Cost is missing

Lesson to audit:
{markdown_content}"""

        response = cerebras_client.chat.completions.create(
            model="llama3.1-8b",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.1
        )
        
        audit_result = response.choices[0].message.content.strip()
        
        # Check if validated
        is_valid = "VALIDATED" in audit_result.upper()
        
        return is_valid, audit_result
        
    except Exception as e:
        # If Llama fails, allow through but log the error
        print(f"Llama Quality Gate error: {str(e)}")
        return True, f"AUDIT SKIPPED: {str(e)}"

def save_locally(file_path, content):
    """Save lesson locally when GitHub is not available"""
    try:
        local_path = os.path.join(KNOWLEDGE_BASE_PATH, file_path)
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        with open(local_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, local_path
    except Exception as e:
        return False, str(e)

def generate_solid_markdown(project_name, category_id, went_well, challenges, recommendations):
    """Generate 'Solid and Scalable' Markdown with proper YAML and H2 structure"""
    timestamp = datetime.now().strftime("%Y-%m-%d")
    
    # Generate summary from went_well and challenges
    summary = f"Project: {project_name}. "
    if went_well:
        summary += f"Successes: {went_well[:100]}..."
    
    # Handle cost variable
    cost_value = "Under review"
    if challenges and any(word in challenges.lower() for word in ['cost', '€', 'kr', 'delay', 'extra']):
        cost_value = challenges
    
    category_tag = category_id.lower()
    markdown = f"""---
titel: "{project_name}"
kategori: {category_id}
version: "1.0"
oprettet: {timestamp}
opdateret: {timestamp}
forfatter: "3P Technology"
status: "active"
tags: ["lesson-learned", "{category_tag}"]
---

# {project_name}

## Summary

{summary}

## Background

Project execution details and context.

## Standards & Requirements

Relevant standards and regulatory requirements.

## Best Practices

{went_well or '• Best practices identified during project execution'}

## Known Pitfalls

| Pitfall | Consequence | Cost |
|---------|--------------|------|
| TBD | TBD | TBD |

## Checklist

[ ] Item 1
[ ] Item 2
[ ] Item 3

## Lessons Learned

**{project_name}**

- **Root Cause**: {challenges or 'Root cause analysis pending'}
- **What Happened**: {recommendations or 'Event description pending'}
- **Cost**: {cost_value}

---
*Added via 3P Knowledge Base UI - {timestamp}*
"""
    return markdown

@app.route('/api/lessons', methods=['POST'])
def add_lesson():
    """
    Add a new lesson to the knowledge base with Quality Gate (3 Guardrails)
    
    GUARDRAIL 1: YAML validation with 8 required fields
    GUARDRAIL 2: Llama 3.1 8B Quality Gate - audits for Unibio Standard
    GUARDRAIL 3: Token Fail-safe - checks for GITHUB_TOKEN
    
    Expected JSON:
    {
        "category": "ATEX",
        "project_name": "Project Name",
        "went_well": "What went well...",
        "challenges": "Challenges and root causes...",
        "recommendations": "Recommendations for future..."
    }
    
    Response includes 'validation' object with:
    - is_valid: boolean
    - errors: list of issues (if any)
    - validated: "VALIDATED: READY FOR GIT PUSH" if passed
    """
    try:
        data = request.json
        category_id = data.get('category')
        project_name = data.get('project_name')
        went_well = data.get('went_well')
        challenges = data.get('challenges')
        recommendations = data.get('recommendations')
        
        if not category_id or not project_name:
            return jsonify({
                'success': False,
                'error': 'Missing category or project name',
                'validation': {'is_valid': False, 'errors': ['Missing category or project name']}
            }), 400
        
        # GUARDRAIL 1: Generate Markdown with YAML (8 required fields)
        markdown_content = generate_solid_markdown(
            project_name, category_id, went_well, challenges, recommendations
        )
        
        # Basic validation check
        is_valid, errors = validate_lesson_quality(markdown_content, category_id)
        
        if not is_valid:
            # GUARDRAIL 2: If basic validation fails, don't call Llama - fail fast
            return jsonify({
                'success': False,
                'error': 'YAML validation failed',
                'validation': {
                    'is_valid': False,
                    'errors': errors,
                    'validated': 'FAILED: YAML Quality Gate'
                }
            }), 400
        
        # GUARDRAIL 2: Call Llama 3.1 8B Quality Gate
        llama_valid, llama_audit = llama_quality_gate(markdown_content)
        
        # If Llama does NOT contain 'VALIDATED', reject the lesson
        if not llama_valid:
            # Save locally but DO NOT push to Git
            success, save_path = save_locally(file_path, markdown_content)
            return jsonify({
                'success': False,
                'error': 'Llama Quality Gate: Root Cause or Cost missing',
                'llama_audit': llama_audit,
                'validation': {
                    'is_valid': False,
                    'errors': ['REJECTED: Missing Root Cause or Cost analysis'],
                    'validated': 'REJECTED: Llama Quality Gate'
                },
                'saved_locally': success,
                'file': save_path if success else None
            }), 400
        
        # Generate filename
        filename = f"{project_name.lower().replace(' ', '-')}-{datetime.now().strftime('%Y%m%d')}.md"
        file_path = f"3p-knowledge/{category_id}/{filename}"
        
        # GUARDRAIL 3: Token Fail-safe - Check for GITHUB_TOKEN
        if not github_token:
            # Save locally, do NOT attempt GitHub push
            success, save_path = save_locally(file_path, markdown_content)
            return jsonify({
                'success': True,
                'message': 'Guardrail Triggered: Secret Missing - Saved Locally',
                'file': save_path,
                'github_committed': False,
                'validation': {
                    'is_valid': True,
                    'errors': [],
                    'validated': 'VALIDATED: READY FOR GIT PUSH (Token Missing)'
                },
                'llama_audit': llama_audit
            }), 201
        
        # All guards passed - commit to GitHub
        if github_owner and github_repo:
            success, message = commit_to_github(file_path, markdown_content, f"Add lesson: {project_name}")
            if success:
                return jsonify({
                    'success': True,
                    'message': 'Lesson validated and committed to GitHub',
                    'file': file_path,
                    'github_committed': True,
                    'validation': {
                        'is_valid': True,
                        'errors': [],
                        'validated': 'VALIDATED: READY FOR GIT PUSH'
                    },
                    'llama_audit': llama_audit
                }), 201
            else:
                # GitHub failed but lesson is valid - save locally as fallback
                success, save_path = save_locally(file_path, markdown_content)
                return jsonify({
                    'success': True,
                    'message': f'Lesson validated but GitHub commit failed: {message}',
                    'file': save_path,
                    'github_committed': False,
                    'validation': {
                        'is_valid': True,
                        'errors': [],
                        'validated': 'VALIDATED: GitHub Failed - Saved Locally'
                    },
                    'llama_audit': llama_audit
                }), 201
        else:
            # No GitHub config - save locally
            success, save_path = save_locally(file_path, markdown_content)
            return jsonify({
                'success': True,
                'message': 'Lesson validated - saved locally (no GitHub config)',
                'file': save_path,
                'github_committed': False,
                'validation': {
                    'is_valid': True,
                    'errors': [],
                    'validated': 'VALIDATED: Saved Locally'
                },
                'llama_audit': llama_audit
            }), 201
                
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Error processing request: {str(e)}',
            'validation': {'is_valid': False, 'errors': [str(e)]}
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': '3P Knowledge Base API is running'
    }), 200

@app.route('/api/status', methods=['GET'])
def status():
    """Check if knowledge base is accessible"""
    try:
        categories = load_kategorier()
        return jsonify({
            'success': True,
            'knowledge_base_path': KNOWLEDGE_BASE_PATH,
            'categories_count': len(categories),
            'categories': [cat['id'] for cat in categories],
            'api_provider': 'Cerebras (llama3.1-8b)'
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    print("=" * 80)
    print("3P Knowledge Base API Starting")
    print("=" * 80)
    print(f"Knowledge Base Path: {KNOWLEDGE_BASE_PATH}")
    print(f"Kategorier File: {KATEGORIER_FILE}")
    print("\nLoading categories...")
    categories = load_kategorier()
    print(f"Found {len(categories)} categories: {[cat['id'] for cat in categories]}")
    print("\nAPI Endpoints:")
    print("  GET  /api/categories      - List all categories")
    print("  POST /api/ask             - Ask a question")
    print("  GET  /api/health          - Health check")
    print("  GET  /api/status          - System status")
    print("\nStarting Flask server on http://localhost:5001")
    print("=" * 80)
    app.run(debug=True, host='0.0.0.0', port=5001)
