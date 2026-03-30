from main import add_task, complete_task, delete_task

def test_add_task():
    tasks = []

    add_task(tasks, "Learn pytest")

    assert len(tasks) == 1
    assert tasks[0]["title"] == "Learn pytest"
    assert tasks[0]["done"] is False

def test_complete_task_success():
    tasks = [{"title": "Learn pytest", "done": False}]
    result = complete_task(tasks, 0)
    assert result is True
    assert tasks[0]["done"] is True

def test_complete_task_invalid_index():
    tasks = [{"title": "Learn pytest", "done": False}]
    result = complete_task(tasks, 5)
    assert result is False
    assert tasks[0]["done"] is False

def test_delete_task_success():
    tasks = [
        {"title": "Task 1", "done": False},
        {"title": "Task 2", "done": False},
        {"title": "Task 3", "done": False},
    ]
    deleted = delete_task(tasks, 0)
    assert deleted == {"title": "Task 1", "done": False}
    assert len(tasks) == 2
    assert tasks[0]["title"] == "Task 2"
    assert tasks[1]["title"] == "Task 3"

def test_delete_task_invalid_index():
    tasks = [
        {"title": "Task 1", "done": False},
        {"title": "Task 2", "done": False},
        {"title": "Task 3", "done": False},
    ]
    deleted = delete_task(tasks, 3)
    assert deleted is None
    assert len(tasks) == 3






