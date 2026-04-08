from textual.app import App, ComposeResult
from textual.widgets import Footer, Header 

class TaskCLI(App):
    CSS_PATH = "assets/style.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield TaskList(id="main list")
        yield ActionZone(id = "actionzone")
        yield Footer()
     