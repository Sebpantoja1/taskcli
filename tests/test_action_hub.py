# tests/test_action_hub.py
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from textual.app import App, ComposeResult
from src.ui.widgets.action_hub import ActionHub

class TestApp(App):
    def compose(self) -> ComposeResult:
        yield ActionHub()

if __name__ == "__main__":
    app = TestApp()
    app.run()