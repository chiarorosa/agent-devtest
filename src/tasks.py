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
