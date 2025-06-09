from crewai import Agent
from langchain_openai import ChatOpenAI


class CustomAgents:
    def __init__(self, llm=None):
        self.llm = llm or ChatOpenAI(model="gpt-3.5-turbo", temperature=0.1)

    def researcher(self) -> Agent:
        """Agent responsável por pesquisar frameworks de agentes."""
        return Agent(
            role="Pesquisador",
            goal="Pesquisar frameworks de orquestração de agentes em Python",
            backstory=(
                "Especialista em tendências de IA e automações que sabe encontrar as "
                "melhores bibliotecas open source."
            ),
            allow_delegation=False,
            llm=self.llm,
            verbose=True,
        )

    def writer(self) -> Agent:
        """Agent responsável por escrever o resumo das pesquisas."""
        return Agent(
            role="Redator",
            goal="Escrever um resumo sobre frameworks de agentes",
            backstory=(
                "Profissional de comunicação focado em tecnologia e inovação."),
            allow_delegation=False,
            llm=self.llm,
            verbose=True,
        )
