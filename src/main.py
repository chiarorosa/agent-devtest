from crewai import Crew, Process
from agents import CustomAgents
from tasks import CustomTasks


class ExampleCrew:
    def run(self) -> str:
        agents = CustomAgents()
        tasks = CustomTasks()

        researcher = agents.researcher()
        writer = agents.writer()

        task_research = tasks.research_frameworks(researcher)
        task_write = tasks.write_summary(writer)

        crew = Crew(
            agents=[researcher, writer],
            tasks=[task_research, task_write],
            process=Process.sequential,
            verbose=True,
        )

        return crew.kickoff()


if __name__ == "__main__":
    result = ExampleCrew().run()
    print(result)
