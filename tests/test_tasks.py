from tasks.models import Task
from tasks.storage import save_tasks, load_tasks

def test_save_and_load(tmp_path):
    path = tmp_path / "data.json"
    tasks = [Task(1, "Test task")]
    # Passo o caminho explicitamente para evitar usar o arquivo default
    save_tasks(tasks, path=str(path))
    loaded = load_tasks(path=str(path))
    assert len(loaded) == 1
    assert isinstance(loaded[0], Task)
    assert loaded[0].title == "Test task"
