# ------------------------------------------------------------
# TRAINEE EXERCISE: Multi-Agent HR System with CrewAI
# ------------------------------------------------------------
# TODO: Implement agents, tasks, and crew
# Reference: https://docs.crewai.com/core-concepts/Agents/
#            https://docs.crewai.com/core-concepts/Tasks/
# ------------------------------------------------------------

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
from app.logging_config import get_logger

logger = get_logger(__name__)


@CrewBase
class HRCrew:
    """HR Crew with three agents: CV Reader, CV Analyzer, Job Matcher"""

    agents: List[BaseAgent]
    tasks: List[Task]

    def __init__(self) -> None:
        """Initialize the crew and load knowledge sources."""
        # TODO: Load job descriptions from knowledge/ folder
        # TODO: Create JSONKnowledgeSource and assign to self.job_sources
        pass

    # ===================== AGENTS =====================

    @agent
    def cv_reader(self) -> Agent:
        """CV Reader Agent - extracts text from PDF files."""
        # TODO: Return Agent with config and tools
        pass

    @agent
    def cv_analyzer(self) -> Agent:
        """CV Analyzer Agent - analyzes and structures CV data."""
        # TODO: Return Agent with config and tools
        pass

    @agent
    def job_matcher(self) -> Agent:
        """Job Matcher Agent - matches candidates to jobs."""
        # TODO: Return Agent with config, tools, and knowledge sources
        pass

    # ===================== TASKS =====================

    @task
    def cv_reader_task(self) -> Task:
        """Task: PDF → TXT conversion"""
        # TODO: Return Task with config
        pass

    @task
    def cv_analyzer_task(self) -> Task:
        """Task: TXT → Structured JSON"""
        # TODO: Return Task with config and output_json
        pass

    @task
    def job_matching_task(self) -> Task:
        """Task: Match candidates to jobs"""
        # TODO: Return Task with config and output_json
        pass

    # ===================== CREW =====================

    @crew
    def crew(self) -> Crew:
        """Assemble the crew with agents and tasks."""
        # TODO: Return Crew with agents and tasks
        pass
