from main import save_tasks, load_tasks

def test_save_and_load_tasks(tmp_path):
    file_path = tmp_path / "tasks.txt"
    tasks = [
        {"title": "Buy milk", "done": False},
        {"title": "Read book", "done": True},
    ]
    save_tasks(tasks, file_path)
    loaded_tasks = load_tasks(file_path)

    assert loaded_tasks == tasks