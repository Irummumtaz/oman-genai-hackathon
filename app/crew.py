
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



# ------------------------------------------------------------
# Crew
# ------------------------------------------------------------
@CrewBase
class HRCrew():
    """HR Crew that: PDF -> TXT -> JSON -> Eligibility"""

    agents: List[BaseAgent]
    tasks: List[Task]

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
            llm = None,
            reasoning=False
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

    # ===================== CREW =====================

    @crew
    def crew(self) -> Crew:
        """Creates the HR crew with 3 sequential tasks."""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )
