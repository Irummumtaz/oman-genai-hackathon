# 🎓 Multi-Agent HR Recruitment System

An intelligent AI-powered system that automates CV screening, analysis, and job matching using **CrewAI** multi-agent framework.

This project is designed as a **hands-on training exercise** for trainees learning Multi-Agent Systems.

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [What Does It Do?](#what-does-it-do)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Running the Application](#running-the-application)
7. [Project Structure](#project-structure)
8. [How It Works](#how-it-works)
9. [For Trainees](#for-trainees)
10. [Troubleshooting](#troubleshooting)

---

## 🎯 Overview

This system uses **three AI agents** working together to:
1. Extract text from PDF resumes
2. Analyze and structure candidate data
3. Match candidates to job openings

**Technology Stack:**
- CrewAI (Multi-agent orchestration)
- Python 3.10+
- OpenAI or Google Gemini (LLM providers)
- Pydantic (Data validation)
- PyPDF2 (PDF processing)

---

## 🤖 What Does It Do?

**Input:**
- PDF resumes (in `CV/` folder)
- Job descriptions in JSON format (in `knowledge/` folder)

**Output:**
- Extracted text files (`preprocessed-CVs/`)
- Structured candidate profiles (`processed-CVs/`)
- Job match reports with scores (`job-matches-results/`)

**Workflow:**
```
PDF CVs → Agent 1 (Extract) → TXT Files
          ↓
TXT Files → Agent 2 (Analyze) → Structured JSON + Assessment
          ↓
JSON + Job Descriptions → Agent 3 (Match) → Match Reports + Scores
```

---

## ✅ Prerequisites

Before you begin, ensure you have:

### 1. **Python 3.10 or higher**
Check your Python version:
```bash
python --version
# or
python3 --version
```

If you need to install Python, visit: https://www.python.org/downloads/

### 2. **pip (Python package manager)**
Usually comes with Python. Check with:
```bash
pip --version
```

### 3. **Git** (optional, for cloning)
```bash
git --version
```

### 4. **API Keys** (choose one)

You need an API key from either:

**Option A: OpenAI**
- Create account at https://platform.openai.com/
- Generate API key at https://platform.openai.com/api-keys
- Cost: ~$0.50-2.00 per run (depends on CV count)

**Option B: Google Gemini** (Recommended for trainees)
- Create account at https://makersuite.google.com/
- Generate API key at https://makersuite.google.com/app/apikey
- Cost: Free tier available (2500 requests/month)

---

## 📦 Installation

### Step 1: Clone or Download the Repository

**Option A: Clone with Git**
```bash
git clone <repository-url>
cd aws-oman-hackathon
```

**Option B: Download ZIP**
- Download and extract the ZIP file
- Open terminal in the extracted folder

### Step 2: Create a Virtual Environment

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` in your terminal prompt.

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `crewai` - Multi-agent framework
- `crewai-tools` - File and directory tools
- `pydantic` - Data validation
- `PyPDF2` - PDF processing
- `python-dotenv` - Environment variables
- And other dependencies

**Wait for installation to complete** (1-3 minutes).

---

## ⚙️ Configuration

### Step 1: Create Environment File

Copy the example environment file:

**On macOS/Linux:**
```bash
cp .env.example .env
```

**On Windows:**
```bash
copy .env.example .env
```

### Step 2: Add Your API Keys

Open `.env` file in a text editor and add your API keys:

**For OpenAI:**
```bash
# .env file
MODEL=openai/gpt-4o-mini
OPENAI_API_KEY=sk-your-openai-api-key-here
```

**For Google Gemini:**
```bash
# .env file
MODEL=gemini/gemini-2.0-flash-exp
GEMINI_API_KEY=your-gemini-api-key-here
```

**Replace the placeholder values with your actual API keys.**

### Step 3: Prepare Input Data

#### Create Required Folders
```bash
mkdir -p CV knowledge preprocessed-CVs processed-CVs job-matches-results
```

#### Add Sample CV (PDF format)
Place your PDF resume files in the `CV/` folder:
```
CV/
├── candidate1.pdf
├── candidate2.pdf
└── candidate3.pdf
```

#### Add Job Descriptions (JSON format)
Create JSON files in the `knowledge/` folder.

**Example:** `knowledge/ml_engineer.json`
```json
{
  "job_title": "Junior Machine Learning Engineer",
  "required_skills": ["Python", "PyTorch", "TensorFlow", "Machine Learning", "Data Analysis"],
  "required_experience_years": 1,
  "education_level": "bachelor",
  "career_level": "entry"
}
```

**Example:** `knowledge/senior_developer.json`
```json
{
  "job_title": "Senior Software Developer",
  "required_skills": ["Python", "JavaScript", "React", "Node.js", "AWS", "Docker"],
  "required_experience_years": 5,
  "education_level": "bachelor",
  "career_level": "senior"
}
```

---

## 🚀 Running the Application

### Quick Start

1. **Activate your virtual environment** (if not already activated):
   ```bash
   # macOS/Linux
   source venv/bin/activate

   # Windows
   venv\Scripts\activate
   ```

2. **Run the application:**
   ```bash
   python -m app.main
   ```

3. **Wait for completion** (5-10 minutes depending on CV count and LLM provider)

### What Happens During Execution

You'll see logs showing:
```
2025-11-10 12:00:00 | INFO | app.main | Running HRCrew
2025-11-10 12:00:05 | INFO | app.crew | Loaded knowledge sources

# Agent 1: CV Reader
[Agent] CV Reader is working...
✓ Extracted text from candidate1.pdf

# Agent 2: CV Analyzer
[Agent] CV Analyzer is working...
✓ Analyzed candidate1.txt → candidate1.json

# Agent 3: Job Matcher
[Agent] Job Matcher is working...
✓ Matched candidate1 against jobs

2025-11-10 12:10:00 | INFO | app.main | Crew run completed
```

### Check Your Results

After completion, check these folders:

1. **`preprocessed-CVs/`** - Extracted text files
   ```
   preprocessed-CVs/
   ├── candidate1.txt
   ├── candidate2.txt
   └── candidate3.txt
   ```

2. **`processed-CVs/`** - Structured candidate data with AI assessment
   ```
   processed-CVs/
   ├── candidate1.json  # Contains: contact, skills, experience, assessment
   ├── candidate2.json
   └── candidate3.json
   ```

3. **`job-matches-results/`** - Match scores and recommendations
   ```
   job-matches-results/
   ├── candidate1.json  # Match score, breakdown, recommendation
   ├── candidate2.json
   └── candidate3.json
   ```

### Sample Output

**Match Result Example:**
```json
{
  "candidate_name": "John Doe",
  "job_title": "Junior Machine Learning Engineer",
  "overall_score": 82,
  "breakdown": {
    "skills_score": 35,
    "experience_score": 25,
    "education_score": 15,
    "career_level_score": 7
  },
  "skills_matched": ["Python", "PyTorch", "Machine Learning"],
  "skills_missing": ["TensorFlow"],
  "match_category": "strong_match",
  "recommendation": "Strong technical fit. Candidate has 80% skill match. Recommend technical interview."
}
```

---

## 📂 Project Structure

```
aws-oman-hackathon/
│
├── 📄 README.md                 # This file - complete guide
├── 📄 TRAINEE_GUIDE.md          # For trainees doing the exercise
│
├── 📁 app/                      # Main application code
│   ├── 📁 config/
│   │   ├── agents.yaml          # Agent configurations (role, goal, backstory)
│   │   └── tasks.yaml           # Task definitions (description, output)
│   │
│   ├── 📁 tools/
│   │   └── pdf_reader.py        # Custom PDF extraction tool
│   │
│   ├── main.py                  # Main entry point
│   ├── crew.py                  # Agent and crew definitions
│   ├── model.py                 # Pydantic data models
│   └── logging_config.py        # Structured logging setup
│
├── 📁 CV/                       # INPUT: Place PDF resumes here
├── 📁 knowledge/                # INPUT: Place job descriptions (JSON) here
│
├── 📁 preprocessed-CVs/         # OUTPUT: Extracted text files
├── 📁 processed-CVs/            # OUTPUT: Structured candidate data
├── 📁 job-matches-results/      # OUTPUT: Match reports
│
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment template
└── .env                         # Your API keys (create this)
```

---

## 🔧 How It Works

### Agent 1: CV Reader
**Purpose:** Extract text from PDF files

**Input:** PDF files from `CV/` folder
**Process:** Uses PyPDF2 to extract text content
**Output:** Text files saved to `preprocessed-CVs/`
**Tools:** DirectoryReadTool, PDFReaderTool

### Agent 2: CV Analyzer
**Purpose:** Analyze CVs and create structured data

**Input:** Text files from `preprocessed-CVs/`
**Process:**
- Extracts structured data (contact, education, experience, skills)
- Calculates career metrics (years of experience, career level)
- Generates intelligent assessment:
  - Overall rating and score
  - Strengths and weaknesses
  - Red flags
  - Suitable roles
  - Interview focus areas

**Output:** JSON files in `processed-CVs/` following `CandidateCV` schema
**Tools:** DirectoryReadTool, FileReadTool, FileWriterTool

### Agent 3: Job Matcher
**Purpose:** Match candidates to jobs with scoring

**Input:**
- Candidate JSONs from `processed-CVs/`
- Job descriptions from `knowledge/` (knowledge base via RAG)

**Process:**
- Compares candidate skills vs. job requirements
- Scores match across 4 dimensions:
  - **Skills Match** (40 points max)
  - **Experience Match** (30 points max)
  - **Education Match** (20 points max)
  - **Career Level Fit** (10 points max)
- Generates recommendations

**Output:** Match reports in `job-matches-results/` with:
- Overall score (0-100)
- Score breakdown
- Skills matched/missing
- Match category (strong/moderate/weak)
- Recommendation text

**Tools:** DirectoryReadTool, FileReadTool, FileWriterTool
**Knowledge:** RAG-enabled with job descriptions

---

## 👨‍🎓 For Trainees

### This is a Training Exercise!

This project is designed to teach you Multi-Agent Systems. The complete working code is provided, but **you can learn by implementing it yourself**.

### Learning Path

1. **Read:** `TRAINEE_GUIDE.md` - Overview and objectives
2. **Study:** CrewAI documentation to understand patterns
3. **Review:** `app/model.py` and `app/logging_config.py` as examples
4. **Implement:** Complete the TODO sections in the code

### What You'll Learn

- ✅ Multi-Agent System architecture
- ✅ Agent configuration with YAML
- ✅ Task orchestration and workflows
- ✅ Custom tool development
- ✅ RAG (Retrieval-Augmented Generation)
- ✅ Pydantic data validation
- ✅ Production logging patterns

### Trainee Files

If you want to do the exercise:
- Review `agents.yaml` - How agents are configured
- Review `tasks.yaml` - How tasks are defined
- Review `crew.py` - How agents and tasks connect
- Review `pdf_reader.py` - How custom tools work
- Review `main.py` - How execution flows

### Resources

- `app/logging_config.py` - Structured logging example
- `app/model.py` - Pydantic schema reference
- [CrewAI Documentation](https://docs.crewai.com/) - Official guides and API reference
- [CrewAI Tools](https://docs.crewai.com/core-concepts/Tools/) - Custom tool development
- [Pydantic Documentation](https://docs.pydantic.dev/) - Data validation

---

## 🔍 Troubleshooting

### Common Issues and Solutions

#### 1. **ModuleNotFoundError: No module named 'crewai'**
**Solution:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

#### 2. **API Key Errors**
```
Error: OpenAI API key not found
```
**Solution:**
- Check `.env` file exists
- Verify API key is correct (no extra spaces)
- Make sure you're using the right key for your MODEL setting

#### 3. **FileNotFoundError: knowledge/ or CV/**
**Solution:**
```bash
# Create required folders
mkdir -p CV knowledge preprocessed-CVs processed-CVs job-matches-results

# Add at least one PDF to CV/ folder
# Add at least one JSON job description to knowledge/ folder
```

#### 4. **ValidationError from Pydantic**
```
ValidationError: field required
```
**Solution:**
- The AI agent couldn't generate valid output
- Check your job description JSON is valid
- Try with a simpler CV first
- Ensure API key has sufficient credits

#### 5. **Slow Execution or Timeouts**
**Solution:**
- Use Gemini instead of OpenAI (faster and cheaper)
- Reduce the number of CVs to process
- Check your internet connection
- Verify API rate limits aren't exceeded

#### 6. **Empty or Incorrect Results**
**Solution:**
- Check CV PDFs are readable (not scanned images)
- Verify job descriptions have all required fields
- Check logs for error messages
- Enable verbose mode in code for more details

### Getting Help

1. **Check logs** - They show detailed execution info
2. **Read error messages** - They usually tell you what's wrong
3. **Review documentation** - CrewAI docs have many examples
4. **Check existing code** - Look at `model.py` and `logging_config.py`
5. **Ask instructor** - If you're in a training session

---

## 📊 System Requirements

**Minimum:**
- Python 3.10+
- 4GB RAM
- Internet connection
- API access (OpenAI or Gemini)

**Recommended:**
- Python 3.11+
- 8GB RAM
- Stable internet connection
- Gemini API (for cost-effectiveness)

**Typical Resource Usage:**
- Processing 10 CVs: 5-10 minutes
- API costs: $0.50-2.00 per run (OpenAI) or Free (Gemini)
- Disk space: Minimal (<100MB)

---

## 🎯 Next Steps

After successfully running the application:

1. **Analyze the outputs** - Review the match reports
2. **Add more CVs** - Test with different profiles
3. **Customize job descriptions** - Add your own requirements
4. **Study the code** - Understand how it works
5. **Experiment** - Modify agent behaviors
6. **Extend** - Add a 4th agent (e.g., email notifications)

---

## 📚 Additional Resources

### Documentation
- [CrewAI Official Docs](https://docs.crewai.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [PyPDF2 Tutorial](https://pypdf2.readthedocs.io/)

### Learning Materials
- [Multi-Agent Systems Overview](https://arxiv.org/abs/2308.08155)
- [LLM-based Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)
- [LangChain Concepts](https://python.langchain.com/docs/get_started/introduction)

---

## 📝 License

This project is for educational purposes.

---

## 🙏 Credits

Built for training trainees on Multi-Agent Systems with CrewAI.

**Questions?** Contact your instructor or check the documentation files.

---

**Happy Learning! 🚀**
