from pathlib import Path

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, task, crew

# Serper tool import (works across versions)
try:
    from crewai_tools import SerperDevTool
except ImportError:
    from crewai.tools import SerperDevTool

BASE_DIR = Path(__file__).parent


@CrewBase
class ResearchCrew:
    """Research crew for company research + report"""

    # YAML files are in the same folder as crew.py
    agents_config = str(BASE_DIR / "agents.yaml")
    tasks_config = str(BASE_DIR / "tasks.yaml")

    # -------- Agents --------
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            tools=[SerperDevTool()],
            verbose=True,
        )

    @agent
    def analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["analyst"],
            verbose=True,
        )

    # -------- Tasks --------
    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config["research_task"])

    @task
    def analysis_task(self) -> Task:
        return Task(config=self.tasks_config["analysis_task"])

    # -------- Crew --------
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
