# 🎓 Multi-Agent HR Recruitment System

An intelligent AI-powered system that automates CV screening, analysis, and job matching using **CrewAI** multi-agent framework.

This project is designed as a **hands-on training exercise** for trainees learning Multi-Agent Systems.

---

## 🚀 Quick Start

**Want to run it right away?** Follow these 5 simple steps:

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up your API key:**
   - Create a `.env` file in the project root
   - Add your API key (see [Configuration](#-configuration) below)

3. **Prepare test data:**
   - Add PDF resumes to `CV/` folder
   - Add job descriptions (JSON) to `knowledge/` folder

4. **Run the application:**
   ```bash
   python -m app.main
   ```

5. **Check results:**
   - `preprocessed-CVs/` - Extracted text files
   - `processed-CVs/` - Structured candidate data
   - `job-matches-results/` - Match scores and recommendations

**That's it!** The application will process all CVs and generate match reports automatically.

---

## 📋 Table of Contents

1. [Prerequisites](#-prerequisites)
2. [Installation](#-installation)
3. [Configuration](#-configuration)
4. [How to Run](#-how-to-run)
5. [How to Test](#-how-to-test)
6. [Understanding the Output](#-understanding-the-output)
7. [Project Structure](#-project-structure)
8. [How It Works](#-how-it-works)
9. [Troubleshooting](#-troubleshooting)

---

## ✅ Prerequisites

Before you begin, make sure you have:

- **Python 3.10 or higher** - Check with `python --version` or `python3 --version`
- **pip** (Python package manager) - Usually comes with Python
- **API Key** Will be provided during the session

---

## 📦 Installation

### Step 1: Create Virtual Environment

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

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install all required packages (CrewAI, PyPDF2, Pydantic, etc.). Wait 1-3 minutes for installation to complete.

---

## ⚙️ Configuration

### Step 1: Create Environment File

Create a `.env` file in the project root directory.

**On macOS/Linux:**
```bash
touch .env
```

**On Windows:**
```bash
type nul > .env
```

Or simply create it using any text editor.

### Step 2: Add Your API Key

Open the `.env` file and add your API key configuration:
```bash
MODEL=openai/gpt-4o-mini
OPENAI_API_KEY=sk-your-openai-api-key-here
```

**Important:** Replace `sk-your-openai-api-key-here` with your actual API key.

### Step 3: Create Required Folders

```bash
mkdir -p CV knowledge preprocessed-CVs processed-CVs job-matches-results
```

### Step 4: Add Test Data

#### Add PDF Resumes
Place at least one PDF resume file in the `CV/` folder:
```
CV/
└── candidate1.pdf
```

#### Add Job Descriptions
Create at least one JSON file in the `knowledge/` folder with job requirements.

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

## 🏃 How to Run

### Basic Run

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

3. **Wait for completion** (typically 5-10 minutes depending on number of CVs and LLM provider)

### What You'll See

During execution, you'll see logs showing the progress:

```
2025-11-10 12:00:00 | INFO | app.main | Running HRCrew
2025-11-10 12:00:05 | INFO | app.crew | Loaded knowledge sources

[Agent] CV Reader is working...
✓ Extracted text from candidate1.pdf

[Agent] CV Analyzer is working...
✓ Analyzed candidate1.txt → candidate1.json

[Agent] Job Matcher is working...
✓ Matched candidate1 against jobs

2025-11-10 12:10:00 | INFO | app.main | Crew run completed
```

The system processes CVs through three agents:
1. **CV Reader** - Extracts text from PDFs
2. **CV Analyzer** - Structures and analyzes CV data
3. **Job Matcher** - Matches candidates to job openings

---

## 🧪 How to Test

### Test Setup

To verify everything works correctly:

1. **Verify your setup:**
   ```bash
   # Check Python version
   python --version  # Should be 3.10+
   
   # Check virtual environment is active
   # You should see (venv) in your prompt
   
   # Check dependencies are installed
   pip list | grep crewai  # Should show crewai package
   ```

2. **Verify configuration:**
   ```bash
   # Check .env file exists and has API key
   cat .env  # macOS/Linux
   type .env  # Windows
   ```

3. **Verify test data:**
   ```bash
   # Check CV folder has at least one PDF
   ls CV/  # macOS/Linux
   dir CV  # Windows
   
   # Check knowledge folder has at least one JSON
   ls knowledge/  # macOS/Linux
   dir knowledge  # Windows
   ```

### Running a Test

1. **Start with one CV:**
   - Place a single PDF file in `CV/` folder
   - Place at least one job description in `knowledge/` folder

2. **Run the application:**
   ```bash
   python -m app.main
   ```

3. **Verify outputs:**
   After completion, check that these folders contain files:
   - `preprocessed-CVs/` - Should have `.txt` files
   - `processed-CVs/` - Should have `.json` files
   - `job-matches-results/` - Should have `.json` files with match scores

### Expected Test Results

**Success indicators:**
- ✅ No errors in the terminal output
- ✅ Files created in all three output folders
- ✅ JSON files contain valid data (open and check them)
- ✅ Match scores are between 0-100

**If something fails:**
- Check the [Troubleshooting](#-troubleshooting) section below
- Review error messages in the terminal
- Verify your API key is correct and has credits

---

## 📊 Understanding the Output

### Output Folders

After running, you'll find results in three folders:

#### 1. `preprocessed-CVs/` - Extracted Text Files
Contains plain text extracted from PDF resumes:
```
preprocessed-CVs/
├── candidate1.txt
├── candidate2.txt
└── candidate3.txt
```

#### 2. `processed-CVs/` - Structured Candidate Data
Contains structured JSON with candidate information and AI assessment:
```
processed-CVs/
├── candidate1.json
├── candidate2.json
└── candidate3.json
```

Each JSON file contains:
- Contact information
- Skills list
- Work experience
- Education
- AI-generated assessment (strengths, weaknesses, rating)

#### 3. `job-matches-results/` - Match Reports
Contains match scores and recommendations for each candidate:
```
job-matches-results/
├── candidate1.json
├── candidate2.json
└── candidate3.json
```

### Sample Match Result

Open any file in `job-matches-results/` to see a match report:

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

**Score Breakdown:**
- **Overall Score**: 0-100 (higher is better)
- **Skills Score**: 0-40 (based on required skills match)
- **Experience Score**: 0-30 (based on years of experience)
- **Education Score**: 0-20 (based on education level)
- **Career Level Score**: 0-10 (based on career level fit)

**Match Categories:**
- `strong_match`: Score 70-100
- `moderate_match`: Score 50-69
- `weak_match`: Score 0-49

---

## 📂 Project Structure

```
oman-genai-hackathon/
│
├── 📄 README.md                 # This file
├── 📄 TRAINEE_GUIDE.md          # Detailed guide for trainees
│
├── 📁 app/                      # Main application code
│   ├── 📁 config/
│   │   ├── agents.yaml          # Agent configurations
│   │   └── tasks.yaml           # Task definitions
│   │
│   ├── 📁 tools/
│   │   └── pdf_reader.py        # Custom PDF extraction tool
│   │
│   ├── main.py                  # Main entry point (run this!)
│   ├── crew.py                  # Agent and crew definitions
│   ├── model.py                 # Data models (Pydantic schemas)
│   └── logging_config.py        # Logging setup
│
├── 📁 CV/                       # INPUT: Place PDF resumes here
├── 📁 knowledge/                # INPUT: Place job descriptions (JSON) here
│
├── 📁 preprocessed-CVs/         # OUTPUT: Extracted text files
├── 📁 processed-CVs/            # OUTPUT: Structured candidate data
├── 📁 job-matches-results/      # OUTPUT: Match reports
│
├── requirements.txt             # Python dependencies
└── .env                         # Your API keys (create this)
```

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
- Processing 1 CV: 1-2 minutes
- Processing 10 CVs: 5-10 minutes
- API costs: $0.50-2.00 per run (OpenAI) or Free (Gemini)
- Disk space: Minimal (<100MB)

---



