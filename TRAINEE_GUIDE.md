# 🎓 Trainee Guide: Multi-Agent System with CrewAI

Welcome to this hands-on training on building Multi-Agent Systems using CrewAI!

---

## 📚 Overview

You'll build an AI-powered HR recruitment system with three agents:
1. **CV Reader** - Extracts text from PDF resumes
2. **CV Analyzer** - Analyzes and structures CV data
3. **Job Matcher** - Matches candidates to jobs

**Total Implementation Time**: 10-16 hours

---

## 🎯 Learning Objectives

- Understand Multi-Agent Systems architecture
- Configure AI agents with roles, goals, and backstories
- Define task workflows in YAML
- Create custom tools for agent capabilities
- Implement RAG with knowledge sources
- Work with structured data using Pydantic
- Apply production-ready logging

---

## 📋 Prerequisites

**Required Knowledge:**
- Python (intermediate level)
- Object-oriented programming
- Basic AI/LLM concepts

**Technical Requirements:**
- Python 3.10+
- API keys (OpenAI or Gemini)
- Text editor or IDE

---

## 🚀 Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure API keys
cp .env.example .env
# Edit .env with your API keys

# 3. Create test data folders
mkdir -p CV knowledge

# 4. Review reference files
# - app/model.py (Pydantic data models)
# - app/logging_config.py (Logging setup)
# - CrewAI documentation (https://docs.crewai.com/)
```

---

## 📝 Implementation Steps

### Step 1: Configure Agents (YAML)
**File**: `app/config/agents.yaml`

Define three agents with:
- `role`: Agent's job title
- `goal`: What the agent should accomplish
- `backstory`: Agent's expertise and context

**Agents to define:**
- `cv_reader` - PDF text extraction
- `cv_analyzer` - CV analysis and structuring
- `job_matcher` - Candidate-job matching

**Reference**: [CrewAI Agent Configuration](https://docs.crewai.com/core-concepts/Agents/)

---

### Step 2: Configure Tasks (YAML)
**File**: `app/config/tasks.yaml`

Define three tasks with:
- `description`: Step-by-step instructions
- `expected_output`: Return value
- `agent`: Which agent executes this task

Use placeholders: `{pdf_files_path}`, `{txt_files_path}`, `{json_files_path}`, `{matches_output_path}`

**Tasks to define:**
- `cv_reader_task` - PDF → TXT
- `cv_analyzer_task` - TXT → JSON
- `job_matching_task` - JSON + Jobs → Match Report

**Reference**: [CrewAI Task Configuration](https://docs.crewai.com/core-concepts/Tasks/)

---

### Step 3: Implement PDF Reader Tool
**File**: `app/tools/pdf_reader.py`

Create a custom CrewAI tool:
- Define `PDFReaderToolInput` with Pydantic
- Implement `PDFReaderTool` class
- Extract text from PDFs using PyPDF2
- Save to output directory

**Key Concepts:**
- Inherit from `BaseTool`
- Define `name`, `description`, `args_schema`
- Implement `_run()` method

---

### Step 4: Implement Agents
**File**: `app/crew.py`

In `HRCrew.__init__()`:
- Load job descriptions from `knowledge/` folder
- Create `JSONKnowledgeSource`

Define three agent methods with `@agent` decorator:
- `cv_reader()` - with DirectoryReadTool, PDFReaderTool
- `cv_analyzer()` - with DirectoryReadTool, FileReadTool, FileWriterTool
- `job_matcher()` - with tools + knowledge sources

**Key Points:**
- Load config with `self.agents_config['agent_name']`
- Set `verbose=True`
- Pass appropriate tools

---

### Step 5: Implement Tasks
**File**: `app/crew.py` (continued)

Define three task methods with `@task` decorator:
- `cv_reader_task()` - Load from task config
- `cv_analyzer_task()` - Add `output_json=CandidateCV`
- `job_matching_task()` - Add `output_json=JobMatchResult`

**Key Points:**
- Load config with `self.tasks_config['task_name']`
- Use `output_json` for structured outputs

---

### Step 6: Implement Crew
**File**: `app/crew.py` (continued)

Define `crew()` method with `@crew` decorator:
- Create `Crew` instance
- Pass `agents=self.agents`
- Pass `tasks=self.tasks`
- Set `verbose=True`

---

### Step 7: Implement Main Execution
**File**: `app/main.py`

Setup logging and implement:
- `run()` function:
  - Create inputs dictionary
  - Log execution start
  - Execute `HRCrew().crew().kickoff(inputs=inputs)`
  - Return results
- `if __name__ == "__main__"` block:
  - Call `run()`
  - Log completion and token usage

---

## ✅ Testing

```bash
# Prepare test data
# 1. Add PDF CVs to CV/ folder
# 2. Add job descriptions to knowledge/ folder

# Example job description (knowledge/ml_engineer.json):
{
  "job_title": "Junior ML Engineer",
  "required_skills": ["Python", "PyTorch", "Machine Learning"],
  "required_experience_years": 1,
  "education_level": "bachelor",
  "career_level": "entry"
}

# Run the system
python -m app.main

# Expected outputs:
# - preprocessed-CVs/*.txt
# - processed-CVs/*.json
# - job-matches-results/*.json
```

---

## 🔧 Troubleshooting

**Common Issues:**

| Error | Solution |
|-------|----------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `KeyError: 'agent_name'` | Check YAML syntax and agent names |
| `FileNotFoundError` | Create CV/ and knowledge/ folders |
| `ValidationError` | Check Pydantic model in model.py |

**Debugging Tips:**
- Enable `verbose=True` in agents and crew
- Check logs for detailed error messages
- Test components individually
- Validate YAML syntax

---

## 📚 Resources

**Essential References:**
- `app/model.py` - Pydantic data models
- `app/logging_config.py` - Logging setup example
- `app/tools/pdf_reader.py` - Example custom tool

**Documentation:**
- [CrewAI Docs](https://docs.crewai.com/)
- [Pydantic Docs](https://docs.pydantic.dev/)
- [PyPDF2 Tutorial](https://pypdf2.readthedocs.io/)

---

## 🏆 Extension Challenges

After completing the basic implementation:
1. Add email notification agent
2. Implement parallel processing
3. Add memory to agents
4. Build a web interface
5. Enhance scoring algorithm
6. Add LinkedIn integration

---

## 📊 Submission Checklist

- [ ] All YAML files configured
- [ ] PDF tool implemented and working
- [ ] All agents defined with tools
- [ ] All tasks defined with configs
- [ ] Crew assembled correctly
- [ ] Main execution runs successfully
- [ ] Sample outputs generated (at least 2 CVs)
- [ ] Logs show successful execution
- [ ] No errors in output

---

## 💡 Tips for Success

1. **Study the documentation** - CrewAI docs have great examples
2. **Test incrementally** - Run after each major step
3. **Review existing code** - Check `logging_config.py`, `model.py`, and `pdf_reader.py`
4. **Check logs** - They tell you what's happening
5. **Validate YAML** - Syntax errors are common
6. **Ask for help** - When stuck, consult your instructor
7. **Be creative** - There's no single "right" way

---

Good luck and happy coding! 🚀

**Questions?** Check the CrewAI documentation or consult your instructor.
