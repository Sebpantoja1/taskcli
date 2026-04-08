# tests/test_widgets.py
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from textual.app import App, ComposeResult
from src.ui.widgets.task_list import TaskList
from src.ui.widgets.action_hub import ActionHub
# from src.ui.widgets.timer import Timer
project_root = Path(__file__).parent.parent
css_path = str(project_root / "assets" / "style.tcss")

class TestApp(App):
    CSS_PATH = css_path
    
    def compose(self) -> ComposeResult:
        yield TaskList()
        yield ActionHub()
        # yield Timer()

if __name__ == "__main__":
    app = TestApp()
    app.run()