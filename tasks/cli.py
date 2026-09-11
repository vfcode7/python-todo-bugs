import argparse
from .storage import load_tasks, save_tasks

def create_task(title):
    tasks = load_tasks()
    new_id = len(tasks) + 1
    # BUG intencional: Task não foi importado aqui (NameError)
    task = Task(new_id, title)
    tasks.append(task)
    save_tasks(tasks)

def main():
    parser = argparse.ArgumentParser(description="Gerenciador de tarefas simples")
    parser.add_argument('--add', nargs=1, help='Adiciona uma nova tarefa')
    parser.add_argument('--list', action='store_true', help='Lista tarefas')
    args = parser.parse_args()

    if args.add:
        create_task(args.add[0])
    # BUG intencional: nome do atributo com typo (args.lilst) -> nunca será True
    elif args.lilst:
        for t in load_tasks():
            print(t)
