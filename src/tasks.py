from scholarly import search_papers
from crewai import Task


class CustomTasks:
    """Conjunto de tarefas da aplicação."""

    def research_frameworks(self, agent: "Agent") -> Task:
        return Task(
            description=(
                "Listar bibliotecas Python para agentes de IA, mencionando o crewAI "
                "e outras opções relevantes."
            ),
            expected_output="Lista de frameworks e breve descrição",
            agent=agent,
        )

    def write_summary(self, agent: "Agent") -> Task:
        return Task(
            description="Gerar um resumo curto a partir das informações coletadas",
            expected_output="Parágrafo explicativo sobre as bibliotecas",
            agent=agent,
        )

    def search_academic_papers(self, agent: "Agent", query: str) -> Task:
        return Task(
            description=(
                f"Pesquisar artigos nas bases IEEE e ACM usando a query '{query}'. "
                "Gerar uma lista com título, DOI, resumo e palavras-chave."
            ),
            expected_output="Lista de artigos pesquisados",
            agent=agent,
            tools=[search_papers],
        )

    def study_papers(self, agent: "Agent") -> Task:
        return Task(
            description=(
                "Analise os artigos coletados destacando metodologias, resultados e "
                "contribuições principais para uma revisão sistemática da literatura."
            ),
            expected_output="Estudo detalhado dos artigos",
            agent=agent,
        )
