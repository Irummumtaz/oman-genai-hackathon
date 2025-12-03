import glob
from typing import List

from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, task, crew

from crewai_tools import FileReadTool, FileWriterTool, DirectoryReadTool
from app.tools.pdf_reader import PDFReaderTool
from .model import CandidateCV, JobMatchResult
from crewai.knowledge.source.json_knowledge_source import JSONKnowledgeSource
from app.logging_config import get_logger

logger = get_logger(__name__)


@CrewBase
class HRCrew:
    """HR Crew with three agents: CV Reader, CV Analyzer, Job Matcher"""

    agents: List[Agent]
    tasks: List[Task]

    def __init__(self) -> None:
        """Initialize the crew and load knowledge sources."""
        # Paths used by tasks (simple defaults — change as you like)
        self.pdf_files_path = "CV"
        self.txt_files_path = "preprocessed-CVs"
        self.json_files_path = "processed-CVs"
        self.matches_output_path = "job-matches-results"
        self.knowledge_path_glob = "knowledge/*.json"

        # Load job descriptions from knowledge/ folder into JSONKnowledgeSource
        files = glob.glob("knowledge/knowledge/*.json")
        logger.info("Loading job knowledge files: %s", files)
        self.job_sources = [JSONKnowledgeSource(file_paths=[fp]) for fp in files]
    # ===================== AGENTS =====================

    @agent
    def cv_reader(self) -> Agent:
        """CV Reader Agent - extracts text from PDF files."""
        # Tools: PDF reader to extract text, FileWriter to save .txt outputs
        tools = [
            PDFReaderTool(),            # expects a PDF path -> text
            FileWriterTool(),           # write text -> file
            DirectoryReadTool()         # optionally list files in the input dir
        ]

        return Agent(
            role="Resume Parsing Specialist",
            goal=(
                "Read PDF resumes from the provided directory, extract text, "
                "clean and normalize text, and save one TXT file per resume "
                f"into {self.txt_files_path}."
            ),
            backstory=(
                "Experienced in document parsing and normalization. Handles messy "
                "PDFs, extracts structured text fields (name, contacts, sections)."
            ),
            tools=tools,
            verbose=True,
            allow_delegation=False,
        )

    @agent
    def cv_analyzer(self) -> Agent:
        """CV Analyzer Agent - analyzes and structures CV data."""
        # Tools: read TXT files and write JSON candidate profiles
        tools = [
            FileReadTool(),     # read extracted txt
            FileWriterTool(),   # write structured json
        ]

        return Agent(
            role="Candidate Profile Analyst",
            goal=(
                "Read cleaned TXT files, extract structured fields (skills, experience, "
                "education, projects), infer seniority and matchable keywords, and "
                f"save JSON profiles into {self.json_files_path}."
            ),
            backstory=(
                "Hands-on HR analyst able to convert resume text into structured JSON "
                "suitable for downstream matching and scoring."
            ),
            tools=tools,
            verbose=True,
            allow_delegation=False,
        )

    @agent
    def job_matcher(self) -> Agent:
        """Job Matcher Agent - matches candidates to jobs."""
        # Tools: read JSON candidate profiles and produce match reports
        tools = [
            FileReadTool(),     # read candidate JSON
            FileWriterTool(),   # write match reports
            DirectoryReadTool() # list available job descriptions or profiles
        ]

        return Agent(
            role="Job-to-Candidate Matching Specialist",
            goal=(
                "Compare candidate JSON profiles with job descriptions loaded from knowledge "
                "sources, compute match scores, rank candidates per job, and output a "
                f"consolidated report into {self.matches_output_path}."
            ),
            backstory=(
                "Skilled in semantic matching and skills mapping. Uses job requirements "
                "to compute relevance, experience alignment, and a short justification."
            ),
            tools=tools,
            knowledge_sources=self.job_sources,
            verbose=True,
            allow_delegation=False,
        )

    # ===================== TASKS =====================

    @task
    def cv_reader_task(self) -> Task:
        """Task: PDF → TXT conversion"""
        description = (
            f"Read all PDF resumes from the directory at {self.pdf_files_path}. "
            "For each PDF, extract text, clean/normalize the text, and write a TXT "
            f"file to {self.txt_files_path} with the same base filename."
        )
        expected_output = (
            f"One TXT file per PDF in {self.txt_files_path} containing cleaned resume text."
        )
        return Task(
            name="cv_reader_task",
            description=description,
            expected_output=expected_output,
            agent=self.cv_reader(),
            # meta used by your internal runner to know where to read/write
            inputs={"pdf_files_path": self.pdf_files_path},
            outputs={"txt_files_path": self.txt_files_path},
        )

    @task
    def cv_analyzer_task(self) -> Task:
        """Task: TXT → Structured JSON"""
        description = (
            f"Read TXT files from {self.txt_files_path}. For each file, extract structured "
            "fields (name, contact, skills, experience entries, education, certifications), "
            f"infer seniority level, and write a JSON candidate profile into {self.json_files_path}."
        )
        expected_output = (
            f"One JSON file per candidate in {self.json_files_path} containing structured profile data."
        )
        return Task(
            name="cv_analyzer_task",
            description=description,
            expected_output=expected_output,
            agent=self.cv_analyzer(),
            inputs={"txt_files_path": self.txt_files_path},
            outputs={"json_files_path": self.json_files_path},
        )

    @task
    def job_matching_task(self) -> Task:
        """Task: Match candidates to jobs"""
        description = (
            f"Load JSON candidate profiles from {self.json_files_path} and compare them against "
            "job descriptions in the Crew's knowledge sources. Compute match scores, rank candidates, "
            f"and write a consolidated report to {self.matches_output_path}."
        )
        expected_output = (
            f"A consolidated match report saved at {self.matches_output_path} containing ranked candidates and match explanations."
        )
        return Task(
            name="job_matching_task",
            description=description,
            expected_output=expected_output,
            agent=self.job_matcher(),
            inputs={"json_files_path": self.json_files_path},
            outputs={"matches_output_path": self.matches_output_path},
        )

    # ===================== CREW =====================

    @crew
    def crew(self) -> Crew:
        """Assemble the crew with agents and tasks."""
        return Crew(
            agents=[self.cv_reader(), self.cv_analyzer(), self.job_matcher()],
            tasks=[self.cv_reader_task(), self.cv_analyzer_task(), self.job_matching_task()],
            verbose=True,
        )
