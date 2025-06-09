# Exemplo de agentes com CrewAI

Este repositório apresenta uma estrutura simples que demonstra como utilizar
[CrewAI](https://github.com/crewAIInc/crewAI) para orquestrar agentes colaborativos. Agora, os agentes podem pesquisar em bases acadêmicas (IEEE e ACM via API Crossref) e realizar estudos detalhados dos artigos encontrados.

## Estrutura
``` 
src/
  agents.py      # Definição dos agentes
  tasks.py       # Definição das tarefas
  tools.py       # Ferramentas personalizadas (ex: busca Crossref)
  main.py        # Execução da aplicação
requirements.txt # Dependências Python
```

## Como executar

1. Crie um ambiente virtual e instale as dependências:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Defina a variável `OPENAI_API_KEY` com sua chave da API.
3. Rode o script principal passando a consulta desejada:
   ```bash
   python src/main.py
   ```

O resultado será impresso no terminal ao final da execução.
