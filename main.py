from textual.app import App, ComposeResult
from textual.widgets import Footer, Header 

class TaskCLI(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        

if __name__ == "__main__":
    app = TaskCLI()
    app.run()