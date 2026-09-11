import json
import os
from .models import Task

def load_tasks(path='tasks.json'):
    if not os.path.exists(path):
        return []
    with open(path, 'r') as f:
        data = json.loads(f.read())
    # BUG potencial: os itens no JSON são strings/dicts; aqui eu tento construir Task(**item) sem desserializar created_at
    tasks = [Task(**item) for item in data]
    return tasks

def save_tasks(tasks, path='tasks.json'):
    # BUG intencional: usei json.dumps(..., f) em vez de json.dump(..., f) — nada é escrito no arquivo
    with open(path, 'w') as f:
        json.dumps([t.__dict__ for t in tasks], f)
