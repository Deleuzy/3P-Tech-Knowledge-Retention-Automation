# 3P Knowledge Base API - Documentation for React UI Development

## Overview
The 3P Knowledge Base is a Flask backend API that uses Cerebras LLM (llama3.1-8b) to answer questions about technical knowledge bases. It's designed for engineering documentation in Danish/English multilingual industrial contexts.

## Base URL
```
http://localhost:5001
```

## API Endpoints

### 1. Health Check
**GET** `/api/health`

Returns the health status of the API.

**Response:**
```json
{
  "status": "healthy",
  "message": "3P Knowledge Base API is running"
}
```

### 2. System Status
**GET** `/api/status`

Returns system configuration and available categories.

**Response:**
```json
{
  "success": true,
  "knowledge_base_path": "../3P-Tech-Knowledge-Retention-Automation/3p-knowledge",
  "categories_count": 6,
  "categories": ["ATEX", "NH3", "PLC-SCADA", "EPLAN", "Novo-Nordisk", "Generelt"],
  "api_provider": "Cerebras (llama3.1-8b)"
}
```

### 3. List Categories
**GET** `/api/categories`

Returns a list of all available knowledge categories.

**Response:**
```json
{
  "success": true,
  "categories": [
    {
      "id": "ATEX",
      "name": "ATEX",
      "folder_path": "ATEX",
      "system_prompt": "You are an ATEX (Explosive Atmospheres) expert..."
    },
    {
      "id": "NH3",
      "name": "NH3 (Ammonia)",
      "folder_path": "NH3",
      "system_prompt": "You are an NH3 (Ammonia) refrigeration expert..."
    },
    {
      "id": "PLC-SCADA",
      "name": "PLC & SCADA",
      "folder_path": "PLC-SCADA",
      "system_prompt": "You are a PLC and SCADA systems expert..."
    },
    {
      "id": "EPLAN",
      "name": "EPLAN",
      "folder_path": "EPLAN",
      "system_prompt": "You are an EPLAN electric CAD expert..."
    },
    {
      "id": "Novo-Nordisk",
      "name": "Novo Nordisk",
      "folder_path": "Novo-Nordisk",
      "system_prompt": "You are a Novo Nordisk pharmaceutical facility expert..."
    },
