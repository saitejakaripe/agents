from pathlib import Path
try:
    from crewai_tools import SerperDevTool
except ImportError:
    from crewai.tools import SerperDevTool


from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, task, crew
from crewai_tools import SerperDevTool


BASE_DIR = Path(__file__).parent


@CrewBase
class StockPicker:
    """StockPicker crew"""

    # Your YAML files are in the SAME folder as this crew.py
    agents_config = str(BASE_DIR / "agents.yaml")
    tasks_config = str(BASE_DIR / "tasks.yaml")

    # -------- Agents --------
    @agent
    def trending_company_finder(self) -> Agent:
        return Agent(
            config=self.agents_config["trending_company_finder"],
            tools=[SerperDevTool()],
            verbose=True,
        )

    @agent
    def financial_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["financial_researcher"],
            tools=[SerperDevTool()],
            verbose=True,
        )

    @agent
    def stock_picker(self) -> Agent:
        return Agent(
            config=self.agents_config["stock_picker"],
            verbose=True,
        )

    # -------- Tasks --------
    @task
    def find_trending_companies(self) -> Task:
        return Task(config=self.tasks_config["find_trending_companies"])

    @task
    def research_trending_companies(self) -> Task:
        return Task(config=self.tasks_config["research_trending_companies"])

    @task
    def pick_best_company(self) -> Task:
        return Task(config=self.tasks_config["pick_best_company"])

    # -------- Crew --------
    @crew
    def crew(self) -> Crew:
        manager = Agent(
            config=self.agents_config["manager"],
            allow_delegation=True,
            verbose=True,
        )

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.hierarchical,
            manager_agent=manager,
            verbose=True,
        )
