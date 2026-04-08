from textual.widget import Widget
from textual.widgets import Static
from typing import List
import sys
from pathlib import Path

# add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from models.task import Task
class TaskList(Widget):
    def __init__(self, tasks: List[Task] = None, **kwargs):
        super().__init__(**kwargs)
        self.tasks = tasks or []

    def compose(self):
        if not self.tasks:
            yield Static("No tasks yet. Press 'a' to add one.", id="empty-msg")
        else:
            for task in self.tasks:
                priority_icon = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}.get(task.priority, "⚪")
                state_icon = {"Todo": "⬜", "In Progress": "🟦", "Done": "✅"}.get(task.state, "⬜")
                text = f"{state_icon} {priority_icon} {task.title}"
                yield Static(text, id=f"task-{task.id}")

    def update_tasks(self, tasks: List[Task]):
        self.tasks = tasks
        self.refresh()