Projeto: Gerenciador de tarefas (com bugs propositais)

O que o projeto faz
- Permite adicionar tarefas e salvar/ler de um arquivo JSON.
- Inclui testes pytest que verificam salvar e carregar tarefas.

Como rodar
1. Instale pytest se necessário:
   pip install pytest

2. Execute os testes:
   python -m pytest -q

3. Tente rodar a CLI (após consertar os bugs):
   python main.py --add "Minha tarefa"
   python main.py --list

Nota: este repositório contém bugs intencionais espalhados pelos arquivos. Sua missão é rodar os testes, encontrar e corrigir os erros até que tudo passe.
