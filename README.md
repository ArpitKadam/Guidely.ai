# Guidely.ai

<div align="center">
  <img src="static/img/logo.png" alt="Guidely.ai Logo" width="200"/>
  
  <h3>🌟 AI-Powered Travel Planning Made Simple</h3>
  
  <p>
    <strong>Guidely.ai</strong> is an intelligent AI travel planner that helps you create comprehensive travel itineraries with both mainstream tourist attractions and unique off-the-beaten-path experiences.
  </p>

  [![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue?style=flat-square&logo=github)](https://github.com/ArpitKadam/Guidely.ai)
  [![Python](https://img.shields.io/badge/Python-3.13+-blue?style=flat-square&logo=python)](https://www.python.org/)
  [![FastAPI](https://img.shields.io/badge/FastAPI-0.118.0+-green?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
  [![Flask](https://img.shields.io/badge/Flask-3.1.2+-red?style=flat-square&logo=flask)](https://flask.palletsprojects.com/)
  [![LangGraph](https://img.shields.io/badge/LangGraph-0.6.8+-orange?style=flat-square)](https://langchain.com/langgraph)
  [![License](https://img.shields.io/badge/License-GPL--3.0-yellow?style=flat-square)](LICENSE)

</div>

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🏗️ Architecture](#️-architecture)
- [🛠️ Tech Stack](#️-tech-stack)
- [🚀 Quick Start](#-quick-start)
- [⚙️ Installation](#️-installation)
- [💻 Usage](#-usage)
- [🔗 API Documentation](#-api-documentation)
- [🎯 Project Structure](#-project-structure)
- [🔧 Configuration](#-configuration)
- [🤖 AI Agent Workflow](#-ai-agent-workflow)
- [🧪 Testing](#-testing)
- [📊 Diagrams & Architecture](#-diagrams--architecture)
- [🐛 Troubleshooting](#-troubleshooting)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## ✨ Features

### 🎯 **Dual Planning Approach**
- **Mainstream Tourist Plans**: Popular attractions, must-see destinations, and classic experiences
- **Off-the-Beaten-Path Plans**: Hidden gems, local experiences, and unique adventures

### 🌐 **Real-time Data Integration**
- **Live Weather Data**: Current conditions and forecasts via OpenWeatherMap API
- **Place Search**: Comprehensive location data through Google Places API
- **Currency Conversion**: Real-time exchange rates for budget planning
- **Web Search**: Current information via Tavily Search API

### 💡 **Comprehensive Planning**
- **Accommodations**: Hotel recommendations with pricing
- **Activities**: Curated experiences based on interests
- **Restaurants**: Local dining suggestions and culinary experiences  
- **Transportation**: Options for getting around destinations
- **Budget Calculations**: Detailed cost breakdowns and daily budgets

### 🎨 **Modern Web Interface**
- **Responsive Design**: Beautiful UI that works on all devices
- **Dark/Light Theme**: Automatic theme detection with manual toggle
- **Real-time Chat**: Interactive conversation with the AI agent
- **Chat History**: Persistent storage of conversations

---

## 🏗️ Architecture

<div align="center">
  <img src="diagrams/System Architecture Overview.png" alt="System Architecture Overview" width="800"/>
</div>

Guidely.ai follows a **microservices architecture** with clear separation between frontend and backend:

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend API    │    │  External APIs  │
│   (Flask)       │───▶│   (FastAPI)      │───▶│  - OpenWeather  │
│   - UI/UX       │    │   - AI Agent     │    │  - Tavily Search│
│   - Chat Interface│   │   - Tool Router  │    │  - Currency API │
│   - Theme System│    │   - LLM Chain    │    │  - Places API   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

### Architecture Layers

1. **🎨 Presentation Layer** (`app.py`, `templates/`, `static/`)
   - Flask web application serving the user interface
   - Responsive design with modern CSS and JavaScript
   - Real-time chat interface

2. **🔌 API Gateway Layer** (`main.py`)
   - FastAPI application handling AI processing requests
   - Request/response validation with Pydantic models
   - Error handling and logging

3. **🧠 Business Logic Layer** (`src/agent/`)
   - LangGraph-based agentic workflow
   - Tool orchestration and execution
   - AI reasoning and decision making

4. **🔧 Service Layer** (`src/tools/`, `src/utils/`)
   - External API integrations
   - Utility functions and helpers
   - Data processing and calculations

5. **🏗️ Infrastructure Layer** (`src/config/`, `src/logger/`, `src/exception/`)
   - Configuration management
   - Logging and monitoring
   - Exception handling

---

## 🛠️ Tech Stack

### Backend Technologies
| Technology | Version | Purpose |
|------------|---------|---------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) | 3.13+ | Core programming language |
| ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) | 0.118.0+ | High-performance web framework for AI API |
| ![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white) | 3.1.2+ | Web framework for frontend application |

### AI & ML Stack
| Technology | Version | Purpose |
|------------|---------|---------|
| **LangGraph** | 0.6.8+ | AI agent workflow orchestration |
| **LangChain** | 0.3.27+ | LLM integration and tool management |
| **Groq** | Latest | High-speed LLM inference |
| **Pydantic** | 2.11.9+ | Data validation and serialization |

### External API Integrations
| Service | Purpose |
|---------|---------|
| **Groq LLM** | Primary language model for AI reasoning |
| **Tavily Search** | Real-time web search capabilities |
| **OpenWeatherMap** | Weather data and forecasts |
| **Google Places** | Location search and place details |
| **ExchangeRate API** | Real-time currency conversion |

### Frontend Technologies
| Technology | Purpose |
|------------|----------|
| **HTML5/CSS3** | Modern responsive design |
| **JavaScript (ES6+)** | Interactive functionality |
| **CSS Variables** | Theme system implementation |
| **Markdown Parsing** | Rich content rendering |
| **Local Storage** | Chat history persistence |

### Development & DevOps Tools
| Tool | Purpose |
|------|---------|
| **uv** | Modern Python package management |
| **python-dotenv** | Environment variable management |
| **colorlog** | Enhanced logging with colors |
| **YAML** | Configuration file format |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.13 or higher
- Git
- API keys for external services (see [Configuration](#-configuration))

### Quick Installation
```bash
# 1. Clone the repository
git clone https://github.com/ArpitKadam/Guidely.ai.git
cd Guidely.ai

# 2. Set up Python environment
pip install uv
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install dependencies
uv pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Edit .env with your API keys

# 5. Start the applications
# Terminal 1 - Backend API
python main.py

# Terminal 2 - Frontend Web Server  
python app.py
```

### Access the Application
- **Web Interface**: http://localhost:5000
- **API Documentation**: http://localhost:8000/docs

---

## ⚙️ Installation

<details>
<summary>📦 Detailed Installation Guide</summary>

### Step 1: Clone Repository
```bash
git clone https://github.com/ArpitKadam/Guidely.ai.git
cd Guidely.ai
```

### Step 2: Python Environment Setup
**Option A: Using uv (Recommended)**
```bash
# Install uv package manager
pip install uv

# Create virtual environment
uv venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

**Option B: Using Traditional venv**
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
# Using uv (faster)
uv pip install -r requirements.txt

# Or using traditional pip
pip install -r requirements.txt
```

### Step 4: Environment Configuration
```bash
# Copy example environment file
cp .env.example .env

# Edit .env file with your actual API keys
# Required API keys are listed in the Configuration section below
```

### Step 5: Verify Installation
```bash
# Test core components
python -c "from src.agent.agentic_workflow import GraphBuilder; print('✅ Installation successful!')"
```

</details>

---

## 💻 Usage

### Starting the Application

The application requires two servers running simultaneously:

**Terminal 1 - Backend API Server (FastAPI)**
```bash
python main.py
# Server starts on http://localhost:8000
```

**Terminal 2 - Frontend Web Server (Flask)**
```bash
python app.py
# Server starts on http://localhost:5000
```

### Using the Web Interface

1. **Access Application**: Navigate to `http://localhost:5000`
2. **Chat Interface**: Use the interactive chat to plan your trips
3. **Example Queries**:
   - *"Plan a 7-day romantic trip to Paris in spring with museums and fine dining"*
   - *"5-day adventure in Tokyo with temples, food markets, and modern culture"*
   - *"Week-long backpacking trip to Costa Rica focused on wildlife and beaches"*

### API Usage

**Endpoint**: `POST /query`

```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"query": "Plan a weekend getaway to Barcelona"}'
```

**Python Example**:
```python
import requests

response = requests.post(
    'http://localhost:8000/query',
    json={'query': 'Plan a 3-day trip to Rome with historical sites'}
)

data = response.json()
print(data['answer'])
```

---

## 🔗 API Documentation

<div align="center">
  <img src="diagrams/API Endpoints Diagram.png" alt="API Endpoints" width="600"/>
</div>

### FastAPI Endpoints

#### POST `/query`
**Description**: Main endpoint for travel planning requests

**Request Schema**:
```json
{
  "query": "string (required) - Travel planning request"
}
```

**Response Schema**:
```json
{
  "answer": "string - Comprehensive travel plan in markdown format"
}
```

**Status Codes**:
- `200`: Successful response
- `400`: Invalid request format  
- `500`: Internal server error

### Flask Routes

| Route | Method | Description |
|-------|--------|-----------|
| `/` | GET | Homepage with chat interface |
| `/about` | GET | Project information |
| `/features` | GET | Feature descriptions |
| `/contact` | GET | Contact information |
| `/query` | POST | Proxy to FastAPI backend |

---

## 🎯 Project Structure

```
Guidely.ai/
├── 📁 src/                          # Source code directory
│   ├── 📁 agent/                    # AI Agent implementation
│   │   ├── __init__.py
│   │   └── agentic_workflow.py      # Main LangGraph workflow
│   ├── 📁 config/                   # Configuration management
│   │   ├── __init__.py
│   │   ├── config.yaml              # App configuration
│   │   └── configuration.py         # Config loader utilities
│   ├── 📁 exception/                # Custom exception handling
│   │   └── __init__.py
│   ├── 📁 logger/                   # Logging system
│   │   └── __init__.py
│   ├── 📁 prompts/                  # AI prompts and templates
│   │   ├── __init__.py
│   │   └── system_prompt.py         # Main system prompt
│   ├── 📁 tools/                    # LangChain tools
│   │   ├── __init__.py
│   │   ├── weather_info_tool.py     # Weather API integration
│   │   ├── place_search_tool.py     # Place search functionality
│   │   ├── expense_calculator_tool.py # Budget calculations
│   │   └── currency_converter_tool.py # Currency conversion
│   └── 📁 utils/                    # Utility functions
│       ├── __init__.py
│       ├── models.py                # Pydantic models & LLM loader
│       ├── weather_info.py          # Weather service implementation
│       ├── place_search.py          # Place search service
│       ├── expense_calculator.py    # Calculator utilities
│       └── currency_converter.py    # Currency service
├── 📁 templates/                    # HTML templates
│   ├── base.html                    # Base template
│   ├── index.html                   # Homepage with chat interface
│   ├── about.html                   # About page
│   ├── features.html                # Features page
│   └── contact.html                 # Contact page
├── 📁 static/                       # Static assets
│   ├── 📁 css/
│   │   └── styles.css               # Main stylesheet
│   ├── 📁 js/
│   │   └── main.js                  # Frontend JavaScript
│   └── 📁 img/
│       └── logo.png                 # Application logo
├── 📁 diagrams/                     # Architecture diagrams
├── main.py                          # FastAPI backend server
├── app.py                           # Flask frontend server
├── pyproject.toml                   # Project configuration
├── requirements.txt                 # Python dependencies
├── uv.lock                          # Dependency lock file
├── .env.example                     # Environment variables template
├── .gitignore                       # Git ignore rules
├── .python-version                  # Python version specification
└── README.md                        # Project documentation
```

---

## 🔧 Configuration

### Required Environment Variables

Create a `.env` file based on `.env.example`:

```env
# LLM Configuration
GROQ_API_KEY=your_groq_api_key_here

# External API Keys
GOOGLE_API_KEY=your_google_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
OPENWEATHERMAP_API_KEY=your_openweather_api_key_here
EXCHANGE_RATE_API_KEY=your_exchange_rate_api_key_here
FOURSQUARE_API_KEY=your_foursquare_api_key_here

# Optional Configuration
BACKEND_URL=http://localhost:8000
PORT=5000
```

### API Key Sources

| Service | Sign-up URL | Purpose |
|---------|-------------|---------|
| **Groq** | [groq.com](https://groq.com) | LLM access for AI reasoning |
| **Google Cloud** | [console.cloud.google.com](https://console.cloud.google.com) | Places API for location data |
| **Tavily** | [tavily.com](https://tavily.com) | Search capabilities |
| **OpenWeatherMap** | [openweathermap.org](https://openweathermap.org) | Weather data (free tier available) |
| **ExchangeRate-API** | [exchangerate-api.com](https://exchangerate-api.com) | Currency conversion |

### Application Configuration

The `src/config/config.yaml` file contains application settings:

```yaml
llm:
  groq:
    provider: "groq"
    model_name: "openai/gpt-oss-20b"
```

---

## 🤖 AI Agent Workflow

<div align="center">
  <img src="diagrams/AI Agent Workflow (LangGraph).png" alt="AI Agent Workflow" width="800"/>
</div>

### LangGraph Architecture

The AI agent uses a sophisticated graph-based workflow powered by LangGraph:

<div align="center">
  <img src="diagrams/User Query Processing Flow.png" alt="User Query Processing Flow" width="700"/>
</div>

### Tool Execution Pipeline

<div align="center">
  <img src="diagrams/Tool Execution Pipeline.png" alt="Tool Execution Pipeline" width="700"/>
</div>

### Core Agent Features

1. **🧠 Intelligent Tool Selection**: Automatically determines which tools are needed based on query analysis
2. **⚡ Parallel Execution**: Runs multiple API calls simultaneously for faster responses  
3. **🔄 State Management**: Maintains context across multiple tool interactions
4. **🛠️ Error Recovery**: Gracefully handles tool failures with fallback strategies
5. **📊 Data Integration**: Combines results from multiple sources into coherent plans

### Available Tools

| Tool | Purpose | API Integration |
|------|---------|----------------|
| **🌤️ Weather Info** | Current weather & forecasts | OpenWeatherMap |
| **📍 Place Search** | Attractions, restaurants, hotels | Google Places |
| **💰 Expense Calculator** | Budget calculations | Internal logic |
| **💱 Currency Converter** | Real-time exchange rates | ExchangeRate API |

---

## 🧪 Testing

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-cov black flake8 mypy

# Run unit tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ --cov=src --cov-report=html

# Code formatting
python -m black src/

# Linting
python -m flake8 src/

# Type checking  
python -m mypy src/
```

### Test Structure

```
tests/
├── unit/
│   ├── test_tools.py
│   ├── test_utils.py
│   └── test_agent.py
├── integration/
│   ├── test_api_endpoints.py
│   └── test_workflow.py
└── fixtures/
    └── sample_responses.json
```

---

## 📊 Diagrams & Architecture

The `diagrams/` folder contains comprehensive architectural diagrams:

<details>
<summary>🖼️ View All Architecture Diagrams</summary>

### System Architecture
- **System Architecture Overview.png** - High-level system design
- **Deployment Architecture.png** - Deployment and infrastructure setup

### Component Architecture  
- **Class Diagram - Core Components.png** - Core system components
- **Tool Architecture Diagram.png** - Tool system architecture
- **Frontend Architecture Diagram.png** - Frontend component structure

### Flow Diagrams
- **Data Flow Diagram.png** - Data flow through the system
- **User Query Processing Flow.png** - Query processing pipeline
- **Sequence Diagram - Travel Query Processing.png** - Detailed sequence flow

### Technical Diagrams
- **AI Agent Workflow (LangGraph).png** - LangGraph workflow structure
- **Tool Execution Pipeline.png** - Tool execution process
- **Configuration Management Diagram.png** - Configuration system
- **Error Handling Flow.png** - Error handling strategy
- **Logging and Monitoring Flow.png** - Logging architecture

</details>

### Key Architecture Diagrams

<div align="center">
  <img src="diagrams/Data Flow Diagram.png" alt="Data Flow Diagram" width="600"/>
  <p><em>Data Flow Architecture</em></p>
</div>

<div align="center">
  <img src="diagrams/Tool Architecture Diagram.png" alt="Tool Architecture" width="600"/>
  <p><em>Tool Integration Architecture</em></p>
</div>

<div align="center">
  <img src="diagrams/Configuration Management Diagram.png" alt="Configuration Management" width="500"/>
  <p><em>Configuration Management Diagram</em></p>
</div>

---

## 🐛 Troubleshooting

<details>
<summary>🔧 Common Issues & Solutions</summary>

### API Key Issues

**Problem**: `GROQ_API_KEY not found in environment variables`

**Solution**:
```bash
# Check .env file format
cat .env
# Ensure no spaces around equals sign
GROQ_API_KEY=your_actual_api_key_here
```

### Port Conflicts

**Problem**: `Address already in use: 8000`

**Solutions**:
```bash
# Find and kill process using port (Linux/macOS)
lsof -ti:8000 | xargs kill -9

# Use different port
uvicorn main:app --port 8001

# On Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Import Errors

**Problem**: `ImportError: langchain_groq is not installed`

**Solution**:
```bash
# Reinstall dependencies
pip install --upgrade langchain-groq
# Or using uv
uv pip install langchain-groq --upgrade
```

### Memory Issues

**Problem**: High memory usage during processing

**Solutions**:
- Implement request timeouts
- Use streaming responses for large outputs
- Monitor concurrent requests
- Clear unused variables

### External API Failures

**Problem**: External APIs returning errors

**Solutions**:
- Verify API key validity and quotas
- Check API service status pages
- Implement retry mechanisms
- Add fallback responses

</details>

### Debug Mode

Enable debug logging for troubleshooting:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Performance Monitoring

Monitor application performance:

```bash
# Check API response times
curl -w "@curl-format.txt" -s -o /dev/null http://localhost:8000/query

# Monitor memory usage
python -m memory_profiler main.py
```

---

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### Development Workflow

1. **🍴 Fork the Repository**
   ```bash
   git clone https://github.com/ArpitKadam/Guidely.ai.git
   cd Guidely.ai
   ```

2. **🌿 Create Feature Branch**
   ```bash
   git checkout -b feature/amazing-new-feature
   ```

3. **💻 Make Changes**
   - Follow existing code structure and patterns
   - Add appropriate tests for new functionality
   - Update documentation as needed

4. **✅ Test Changes**
   ```bash
   python -m pytest tests/
   python -m flake8 src/
   python -m black src/ --check
   ```

5. **📤 Commit and Push**
   ```bash
   git add .
   git commit -m "Add: Amazing new feature with comprehensive tests"
   git push origin feature/amazing-new-feature
   ```

6. **🔀 Create Pull Request**
   - Provide clear description of changes
   - Include test results and screenshots
   - Reference any related issues

### Code Standards

- **Python Style**: Follow PEP 8 guidelines
- **Type Hints**: Use type annotations where appropriate
- **Documentation**: Write clear docstrings and comments
- **Testing**: Maintain good test coverage

### Adding New Tools

To extend the system with new tools:

1. **Create Service Implementation** (`src/utils/`)
2. **Create LangChain Tool Wrapper** (`src/tools/`)
3. **Register in Agent Workflow** (`src/agent/`)
4. **Add Tests** (`tests/`)
5. **Update Documentation**

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0** - see the [LICENSE](LICENSE) file for details.

```
Copyright (C) 2024 Arpit Kadam

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
```

---

<div align="center">
  
### 🌟 **Made with ❤️ by [Arpit Kadam](https://github.com/ArpitKadam)**

**GitHub Repository**: https://github.com/ArpitKadam/Guidely.ai

---

*Last Updated: January 2025 | Version: 1.0.0*

**⭐ If you find this project helpful, please consider giving it a star on GitHub!**

</div>
