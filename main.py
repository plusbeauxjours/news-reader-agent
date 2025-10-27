import dotenv

dotenv.load_dotenv()

from crewai import Crew, Agent, Task
from crewai.project import CrewBase, agent, task, crew


@CrewBase
class CreativeWriterCrew:

    @agent
    def creative_writer_agent(self):
        return Agent(
            config=self.agents_config["creative_writer_agent"],
        )

    @task
    def summarize_task(self):
        return Task(
            config=self.tasks_config["summarize_task"],
        )

    @task
    def rewrite_task(self):
        return Task(
            config=self.tasks_config["rewrite_task"],
        )

    @crew
    def assemble_crew(self):
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )

CreativeWriterCrew().assemble_crew().kickoff(
    inputs={
        "text": "The city lights shimmered across the river as the crowd gathered to celebrate the new year.",
    }
)