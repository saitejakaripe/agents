from pathlib import Path
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, task, crew

BASE_DIR = Path(__file__).parent


@CrewBase
class CricketersCrew:
    """Cricketers Crew"""

    agents_config = str(BASE_DIR / "agents.yaml")
    tasks_config = str(BASE_DIR / "tasks.yaml")

    # --------- AGENTS ----------
    @agent
    def virat(self) -> Agent:
        return Agent(config=self.agents_config["virat"], verbose=True)

    @agent
    def dhoni(self) -> Agent:
        return Agent(config=self.agents_config["dhoni"], verbose=True)

    @agent
    def rohit(self) -> Agent:
        return Agent(config=self.agents_config["rohit"], verbose=True)

    @agent
    def selector(self) -> Agent:
        return Agent(config=self.agents_config["selector"], verbose=True)

    # --------- TASKS ----------
    @task
    def virat_draft(self) -> Task:
        return Task(config=self.tasks_config["virat_draft"])

    @task
    def dhoni_draft(self) -> Task:
        return Task(config=self.tasks_config["dhoni_draft"])

    @task
    def rohit_draft(self) -> Task:
        return Task(config=self.tasks_config["rohit_draft"])

    @task
    def pick_best(self) -> Task:
        return Task(config=self.tasks_config["pick_best"])

    # --------- CREW ----------
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
