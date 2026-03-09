import React, { useState, useEffect } from 'react';
import { Send, Plus, FileText, Search, Zap, BookOpen, Loader } from 'lucide-react';

export default function KnowledgeBaseUI() {
  const [categories, setCategories] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('ATEX');
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [tab, setTab] = useState('ask');
  const [error, setError] = useState(null);

  const API_BASE = 'http://localhost:5001';

  // Load categories on mount
  useEffect(() => {
    fetchCategories();
  }, []);

  const fetchCategories = async () => {
    try {
      const res = await fetch(`${API_BASE}/api/categories`);
      const data = await res.json();
      if (data.success && data.categories) {
        setCategories(data.categories);
        if (data.categories.length > 0) {
          setSelectedCategory(data.categories[0].id);
        }
      } else {
        // If API fails, use default categories
        const defaultCategories = [
          { id: 'ATEX', name: 'ATEX' },
          { id: 'NH3', name: 'NH3' },
          { id: 'PLC-SCADA', name: 'PLC-SCADA' },
          { id: 'EPLAN', name: 'EPLAN' },
          { id: 'Novo-Nordisk', name: 'Novo Nordisk' },
          { id: 'Generelt', name: 'General' }
        ];
        setCategories(defaultCategories);
        setSelectedCategory('ATEX');
      }
    } catch (err) {
      console.warn('Could not load categories from API, using defaults');
      // Use default categories if API fails
      const defaultCategories = [
        { id: 'ATEX', name: 'ATEX' },
        { id: 'NH3', name: 'NH3' },
        { id: 'PLC-SCADA', name: 'PLC-SCADA' },
        { id: 'EPLAN', name: 'EPLAN' },
        { id: 'Novo-Nordisk', name: 'Novo Nordisk' },
        { id: 'Generelt', name: 'General' }
      ];
      setCategories(defaultCategories);
      setSelectedCategory('ATEX');
    }
  };

  const handleAsk = async () => {
    if (!question.trim()) return;
    
    setLoading(true);
    setError(null);
    
    try {
      const res = await fetch(`${API_BASE}/api/ask`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          category: selectedCategory,
          question: question
        })
      });

      const data = await res.json();
      
      if (data.success) {
        setResponse(data);
        setQuestion('');
      } else {
        setError(data.error || 'Failed to get answer');
      }
    } catch (err) {
      setError(`Error: ${err.message}`);
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const getCategoryColor = (categoryId) => {
    const colors = {
      'ATEX': 'from-orange-500 to-red-500',
      'NH3': 'from-blue-500 to-cyan-500',
      'PLC-SCADA': 'from-purple-500 to-indigo-500',
      'EPLAN': 'from-green-500 to-emerald-500',
      'Novo-Nordisk': 'from-pink-500 to-rose-500',
      'Generelt': 'from-gray-500 to-slate-500'
    };
    return colors[categoryId] || 'from-blue-500 to-cyan-500';
  };

  const getCategoryIcon = (categoryId) => {
    const icons = {
      'ATEX': '⚡',
      'NH3': '❄️',
      'PLC-SCADA': '🔧',
      'EPLAN': '📐',
      'Novo-Nordisk': '🏭',
      'Generelt': '📋'
    };
    return icons[categoryId] || '📚';
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
      {/* Header */}
      <header className="border-b border-slate-700 bg-slate-900/50 backdrop-blur-sm sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-gradient-to-br from-blue-500 to-cyan-500 rounded-lg flex items-center justify-center">
              <BookOpen className="w-6 h-6 text-white" />
            </div>
            <div>
              <h1 className="text-xl font-bold text-white">3P Knowledge Base</h1>
              <p className="text-xs text-slate-400">Powered by Llama 3.1 8B</p>
            </div>
          </div>
          <button className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg flex items-center gap-2 transition">
            <Plus className="w-4 h-4" />
            New Project
          </button>
        </div>
      </header>

      <div className="max-w-7xl mx-auto px-6 py-8">
        <div className="grid grid-cols-3 gap-6">
          {/* Left Sidebar - Categories */}
          <div className="col-span-1">
            <div className="bg-slate-800 rounded-xl border border-slate-700 p-4 sticky top-24">
              <h2 className="text-sm font-semibold text-white mb-4 flex items-center gap-2">
                <Zap className="w-4 h-4 text-blue-400" />
                Categories
              </h2>
              <div className="space-y-2">
                {categories.map((cat) => (
                  <button
                    key={cat.id}
                    onClick={() => setSelectedCategory(cat.id)}
                    className={`w-full text-left px-4 py-3 rounded-lg transition ${
                      selectedCategory === cat.id
                        ? `bg-gradient-to-r ${getCategoryColor(cat.id)} text-white font-medium`
                        : 'bg-slate-700 text-slate-300 hover:bg-slate-600'
                    }`}
                  >
                    <span className="text-lg mr-2">{getCategoryIcon(cat.id)}</span>
                    {cat.name}
                  </button>
                ))}
              </div>
            </div>
          </div>

          {/* Main Content Area */}
          <div className="col-span-2 space-y-6">
            {/* Tabs */}
            <div className="flex gap-2 border-b border-slate-700">
              <button
                onClick={() => setTab('ask')}
                className={`px-6 py-3 font-medium transition border-b-2 ${
                  tab === 'ask'
                    ? 'border-blue-500 text-blue-400'
                    : 'border-transparent text-slate-400 hover:text-slate-300'
                }`}
              >
                <Search className="w-4 h-4 inline mr-2" />
                Ask Knowledge Base
              </button>
              <button
                onClick={() => setTab('contribute')}
                className={`px-6 py-3 font-medium transition border-b-2 ${
                  tab === 'contribute'
                    ? 'border-blue-500 text-blue-400'
                    : 'border-transparent text-slate-400 hover:text-slate-300'
                }`}
              >
                <Plus className="w-4 h-4 inline mr-2" />
                Add Lessons Learned
              </button>
            </div>

            {/* Error Message */}
            {error && (
              <div className="bg-red-900/20 border border-red-700 rounded-lg p-4">
                <p className="text-red-300 text-sm">{error}</p>
              </div>
            )}

            {/* Tab Content - Ask */}
            {tab === 'ask' && (
              <div className="space-y-6">
                {/* Input Section */}
                <div className="bg-slate-800 rounded-xl border border-slate-700 p-6">
                  <label className="block text-sm font-semibold text-white mb-3">
                    Ask about {categories.find(c => c.id === selectedCategory)?.name}
                  </label>
                  <textarea
                    value={question}
                    onChange={(e) => setQuestion(e.target.value)}
                    placeholder="E.g., What are the common pitfalls in zone classification? What should we estimate for this project type?"
                    className="w-full bg-slate-700 text-white rounded-lg p-4 placeholder-slate-400 border border-slate-600 focus:border-blue-500 focus:outline-none resize-none"
                    rows="4"
                  />
                  <button
                    onClick={handleAsk}
                    disabled={loading || !question.trim()}
                    className="mt-4 w-full bg-gradient-to-r from-blue-600 to-cyan-600 hover:from-blue-700 hover:to-cyan-700 disabled:opacity-50 disabled:cursor-not-allowed text-white font-semibold py-3 rounded-lg flex items-center justify-center gap-2 transition"
                  >
                    {loading ? (
                      <>
                        <Loader className="w-4 h-4 animate-spin" />
                        Retrieving Knowledge...
                      </>
                    ) : (
                      <>
                        <Send className="w-4 h-4" />
                        Ask Knowledge Base
                      </>
                    )}
                  </button>
                </div>

                {/* Response Section */}
                {response && (
                  <div className="bg-slate-800 rounded-xl border border-slate-700 p-6 animate-in fade-in slide-in-from-bottom-4 duration-300">
                    <div className="flex items-start justify-between mb-4">
                      <div>
                        <h3 className="text-lg font-semibold text-white mb-1">
                          Knowledge from {response.category}
                        </h3>
                        <p className="text-xs text-slate-400">
                          {response.files_loaded} documents loaded • Model: {response.model}
                        </p>
                      </div>
                      <FileText className="w-5 h-5 text-blue-400" />
                    </div>
                    <div className="bg-slate-700/50 rounded-lg p-4 border border-slate-600">
                      <p className="text-slate-200 whitespace-pre-wrap leading-relaxed text-sm">
                        {response.answer}
                      </p>
                    </div>
                    <div className="mt-4 flex gap-2">
                      <button 
                        onClick={() => navigator.clipboard.writeText(response.answer)}
                        className="text-xs px-3 py-2 bg-slate-700 hover:bg-slate-600 text-slate-300 rounded transition"
                      >
                        📋 Copy
                      </button>
                      <button className="text-xs px-3 py-2 bg-slate-700 hover:bg-slate-600 text-slate-300 rounded transition">
                        🔗 Share
                      </button>
                    </div>
                  </div>
                )}
              </div>
            )}

            {/* Tab Content - Contribute */}
            {tab === 'contribute' && (
              <div className="bg-slate-800 rounded-xl border border-slate-700 p-6 space-y-4">
                <p className="text-slate-300 text-sm">
                  Help the team learn from this project. Fill in what went well, what went wrong, and what to do next time.
                </p>
                
                <div>
                  <label className="block text-sm font-semibold text-white mb-2">Project Name</label>
                  <input
                    type="text"
                    placeholder="e.g., Unibio Ammonia System"
                    className="w-full bg-slate-700 text-white rounded-lg p-3 placeholder-slate-400 border border-slate-600 focus:border-blue-500 focus:outline-none"
                  />
                </div>

                <div>
                  <label className="block text-sm font-semibold text-white mb-2">What Went Well?</label>
                  <textarea
                    placeholder="Describe successes and best practices discovered..."
                    className="w-full bg-slate-700 text-white rounded-lg p-3 placeholder-slate-400 border border-slate-600 focus:border-blue-500 focus:outline-none"
                    rows="3"
                  />
                </div>

                <div>
                  <label className="block text-sm font-semibold text-white mb-2">Challenges & Root Causes</label>
                  <textarea
                    placeholder="What went wrong? Why did it happen?"
                    className="w-full bg-slate-700 text-white rounded-lg p-3 placeholder-slate-400 border border-slate-600 focus:border-blue-500 focus:outline-none"
                    rows="3"
                  />
                </div>

                <button className="w-full bg-gradient-to-r from-green-600 to-emerald-600 hover:from-green-700 hover:to-emerald-700 text-white font-semibold py-3 rounded-lg transition">
                  Save Lessons to Knowledge Base
                </button>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
