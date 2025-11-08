
import os
from crewai import Agent, Crew, Process, Task
from typing import Any, Dict, List
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import (
    FileReadTool,
    FileWriterTool,
    DirectoryReadTool,
)
from app.tools.pdf_reader import PDFReaderTool
from .model import CandidateCV, JobMatchResult
from crewai.knowledge.source.json_knowledge_source import JSONKnowledgeSource



# ------------------------------------------------------------
# Crew
# ------------------------------------------------------------
@CrewBase
class HRCrew():
    agents: List[BaseAgent]
    tasks: List[Task]

    def __init__(self) -> None:
        jobs = os.listdir("knowledge/")
        self.job_sources = JSONKnowledgeSource(file_paths=jobs)
    
    # ===================== AGENTS =====================
    @agent
    def cv_reader(self) -> Agent:
        return Agent(
            config=self.agents_config['cv_reader'],
            verbose=True,
            tools=[
                DirectoryReadTool(),
                PDFReaderTool(),
            ],
        function_calling_llm="gpt-4o-mini"
        )
    @agent
    def cv_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['cv_analyzer'],
            verbose=True,
            tools=[
                DirectoryReadTool(),
                FileReadTool(),
                FileWriterTool(),
            ],
        )
    @agent
    def job_matcher(self) -> Agent:
        return Agent(
            config=self.agents_config['job_matcher'],
            verbose=True,
            tools=[
                DirectoryReadTool(),
                FileReadTool(),
                FileWriterTool(),
            ],
            knowledge_sources=[self.job_sources],
        )
    # ===================== TASKS =====================
    @task
    def cv_reader_task(self) -> Task:
        """
        Task 1: PDF -> TXT
        Uses {folder_path} and {output_path} from inputs.
        """
        return Task(
            config=self.tasks_config['cv_reader_task'],
            )
    @task
    def cv_analyzer_task(self) -> Task:
        """
        Task 1: TXT -> JSON
        Uses {output_txt} and {output_json} from inputs.
        """
        return Task(
            config=self.tasks_config['cv_analyzer_task'],
            output_json=CandidateCV
            )
    @task
    def job_matching_task(self) -> Task:
        return Task(
            config=self.tasks_config['job_matching_task'],
            output_json=JobMatchResult
            )
    # ===================== CREW =====================
    @crew
    def crew(self) -> Crew:
        """Creates the HR crew with 3 sequential tasks."""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )
