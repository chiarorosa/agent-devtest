from crewai import Crew, Process
from agents import CustomAgents
from tasks import CustomTasks


class ExampleCrew:
    def run(self, query: str) -> str:
        agents = CustomAgents()
        tasks = CustomTasks()

        researcher = agents.researcher()
        analyst = agents.analyst()

        task_search = tasks.search_academic_papers(researcher, query)
        task_study = tasks.study_papers(analyst)

        crew = Crew(
            agents=[researcher, analyst],
            tasks=[task_search, task_study],
            process=Process.sequential,
            verbose=True,
        )

        return crew.kickoff()


if __name__ == "__main__":
    result = ExampleCrew().run("agent frameworks")
    print(result)
