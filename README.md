[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/alperenkocyigit-semantic-scholar-graph-api-badge.png)](https://mseep.ai/app/alperenkocyigit-semantic-scholar-graph-api)

# 📚 Semantic Scholar MCP Server

> **A comprehensive Model Context Protocol (MCP) server for seamless integration with Semantic Scholar's academic database**

[![smithery badge](https://smithery.ai/badge/@alperenkocyigit/semantic-scholar-graph-api)](https://smithery.ai/server/@alperenkocyigit/semantic-scholar-graph-api)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**Maintainer:** [@alperenkocyigit](https://github.com/alperenkocyigit)

This powerful MCP server bridges the gap between AI assistants and academic research by providing direct access to Semantic Scholar's comprehensive database. Whether you're conducting literature reviews, exploring citation networks, or seeking academic insights, this server offers a streamlined interface to millions of research papers.

## 🌟 What Can You Do?

### 🔍 **Advanced Paper Discovery**
- **Smart Search**: Find papers using natural language queries
- **Bulk Operations**: Process multiple papers simultaneously
- **Autocomplete**: Get intelligent title suggestions as you type
- **Precise Matching**: Find exact papers using title-based search

### 🎯 **AI-Powered Recommendations**
- **Smart Paper Recommendations**: Get personalized paper suggestions based on your interests
- **Multi-Example Learning**: Use multiple positive and negative examples to fine-tune recommendations
- **Single Paper Similarity**: Find papers similar to a specific research work
- **Relevance Scoring**: AI-powered relevance scores for better paper discovery

### 👥 **Author Research**
- **Author Profiles**: Comprehensive author information and metrics
- **Bulk Author Data**: Fetch multiple author profiles at once
- **Author Search**: Discover researchers by name or affiliation

### 📊 **Citation Analysis**
- **Citation Networks**: Explore forward and backward citations
- **Reference Mapping**: Understand paper relationships
- **Impact Metrics**: Access citation counts and paper influence

### 💡 **Content Discovery**
- **Text Snippets**: Search within paper content
- **Contextual Results**: Find relevant passages and quotes
- **Full-Text Access**: When available through Semantic Scholar

---

## 🛠️ Quick Setup

### System Requirements
- **Python**: 3.10 or higher
- **Dependencies**: `requests`, `mcp`, `bs4`
- **Network**: Stable internet connection for API access

## 🚀 Installation Options

### ⚡ One-Click Install with Smithery

**For Claude Desktop:**
```bash
npx -y @smithery/cli@latest install @alperenkocyigit/semantic-scholar-graph-api --client claude --config "{}"
```

**For Cursor IDE:**
Navigate to `Settings → Cursor Settings → MCP → Add new server` and paste:
```bash
npx -y @smithery/cli@latest run @alperenkocyigit/semantic-scholar-graph-api --client cursor --config "{}"
```

**For Windsurf:**
```bash
npx -y @smithery/cli@latest install @alperenkocyigit/semantic-scholar-graph-api --client windsurf --config "{}"
```

**For Cline:**
```bash
npx -y @smithery/cli@latest install @alperenkocyigit/semantic-scholar-graph-api --client cline --config "{}"
```

### 🔧 Manual Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/alperenkocyigit/semantic-scholar-graph-api.git
   cd semantic-scholar-graph-api
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server:**
   ```bash
   python semantic_scholar_server.py
   ```

---

## 🔧 Configuration Guide

### Local Setups

#### Claude Desktop Setup

**macOS/Linux Configuration:**
Add to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "semanticscholar": {
      "command": "python",
      "args": ["/path/to/your/semantic_scholar_server.py"]
    }
  }
}
```

**Windows Configuration:**
```json
{
  "mcpServers": {
    "semanticscholar": {
      "command": "C:\\Users\\YOUR_USERNAME\\miniconda3\\envs\\mcp_server\\python.exe",
      "args": ["D:\\path\\to\\your\\semantic_scholar_server.py"],
      "env": {},
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

#### Cline Integration
```json
{
  "mcpServers": {
    "semanticscholar": {
      "command": "bash",
      "args": [
        "-c",
        "source /path/to/your/.venv/bin/activate && python /path/to/your/semantic_scholar_server.py"
      ],
      "env": {},
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

### Remote Setups

#### Auto Configuration
```bash
npx -y @smithery/cli@latest install @alperenkocyigit/semantic-scholar-graph-api --client <valid-client-name> --key <your-smithery-api-key>
```
**Valid client names: [claude,cursor,vscode,boltai]**

#### Json Configuration
**macOS/Linux Configuration:**
```json
{
  "mcpServers": {
    "semantic-scholar-graph-api": {
      "command": "npx",
      "args": [
        "-y",
        "@smithery/cli@latest",
        "run",
        "@alperenkocyigit/semantic-scholar-graph-api",
        "--key",
        "your-smithery-api-key"
      ]
    }
  }
}
```
**Windows Configuration:**
```json
{
  "mcpServers": {
    "semantic-scholar-graph-api": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "@smithery/cli@latest",
        "run",
        "@alperenkocyigit/semantic-scholar-graph-api",
        "--key",
        "your-smithery-api-key"
      ]
    }
  }
}
```
**WSL Configuration:**
```json
{
  "mcpServers": {
    "semantic-scholar-graph-api": {
      "command": "wsl",
      "args": [
        "npx",
        "-y",
        "@smithery/cli@latest",
        "run",
        "@alperenkocyigit/semantic-scholar-graph-api",
        "--key",
        "your-smithery-api-key"
      ]
    }
  }
}
```

---

## 🎯 Available Tools

| Tool | Description | Use Case |
|------|-------------|----------|
| `search_semantic_scholar` | Search papers by query | Literature discovery |
| `search_semantic_scholar_authors` | Find authors by name | Researcher identification |
| `get_semantic_scholar_paper_details` | Get comprehensive paper info | Detailed analysis |
| `get_semantic_scholar_author_details` | Get author profiles | Author research |
| `get_semantic_scholar_citations_and_references` | Fetch citation network | Impact analysis |
| `get_semantic_scholar_paper_match` | Find exact paper matches | Precise searching |
| `get_semantic_scholar_paper_autocomplete` | Get title suggestions | Smart completion |
| `get_semantic_scholar_papers_batch` | Bulk paper retrieval | Batch processing |
| `get_semantic_scholar_authors_batch` | Bulk author data | Mass analysis |
| `search_semantic_scholar_snippets` | Search text content | Content discovery |
| `get_semantic_scholar_paper_recommendations_from_lists` | Get recommendations from positive/negative examples | AI-powered discovery |
| `get_semantic_scholar_paper_recommendations` | Get recommendations from single paper | Similar paper finding |

---

## 💡 Usage Examples

### Basic Paper Search
```python
# Search for papers on machine learning
results = await search_semantic_scholar("machine learning", num_results=5)
```

### Author Research
```python
# Find authors working on natural language processing
authors = await search_semantic_scholar_authors("natural language processing")
```

### Citation Analysis
```python
# Get citation network for a specific paper
citations = await get_semantic_scholar_citations_and_references("paper_id_here")
```

### 🆕 AI-Powered Paper Recommendations

#### Multi-Example Recommendations
```python
# Get recommendations based on multiple positive and negative examples
positive_papers = ["paper_id_1", "paper_id_2", "paper_id_3"]
negative_papers = ["bad_paper_id_1", "bad_paper_id_2"]
recommendations = await get_semantic_scholar_paper_recommendations_from_lists(
    positive_paper_ids=positive_papers,
    negative_paper_ids=negative_papers,
    limit=20
)
```

#### Single Paper Similarity
```python
# Find papers similar to a specific research work
similar_papers = await get_semantic_scholar_paper_recommendations(
    paper_id="target_paper_id",
    limit=15
)
```

#### Content Discovery
```python
# Search for specific text content within papers
snippets = await search_semantic_scholar_snippets(
    query="neural network optimization",
    limit=10
)
```
---

## 📂 Project Architecture

```
semantic-scholar-graph-api/
├── 📄 README.md                    # Project documentation
├── 📋 requirements.txt             # Python dependencies
├── 🔍 search.py   # Core API interaction module
├── 🖥️ server.py   # MCP server implementation
└── 🗂️ __pycache__/                # Compiled Python files
```

### Core Components

- **`search.py`**: Handles all interactions with the Semantic Scholar API, including rate limiting, error handling, and data processing
- **`server.py`**: Implements the MCP server protocol and exposes tools for AI assistant integration

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Ways to Contribute
- 🐛 **Bug Reports**: Found an issue? Let us know!
- 💡 **Feature Requests**: Have ideas for improvements?
- 🔧 **Code Contributions**: Submit pull requests
- 📖 **Documentation**: Help improve our docs

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and test thoroughly
4. Commit your changes: `git commit -m 'Add amazing feature'`
5. Push to the branch: `git push origin feature/amazing-feature`
6. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Semantic Scholar Team** for providing the excellent API
- **Model Context Protocol** community for the framework
- **Contributors** who help improve this project

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/alperenkocyigit/semantic-scholar-graph-api/issues)
- **Discussions**: [GitHub Discussions](https://github.com/alperenkocyigit/semantic-scholar-graph-api/discussions)
- **Maintainer**: [@alperenkocyigit](https://github.com/alperenkocyigit)

---

<div align="center">
  <strong>Made with ❤️ for the research community</strong>
  <br>
  <sub>Empowering AI agents with academic knowledge</sub>
</div>
