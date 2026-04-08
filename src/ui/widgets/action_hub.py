from textual.widget import Widget
from textual.widgets import Input, Button
from textual.containers import Horizontal
from textual.message import Message

class ActionHub(Widget):
    
    def compose(self):
        with Horizontal():

            yield Input(placeholder="Task title...", id="title-input")
            yield Input(placeholder="Description", id="desc-input")
            yield Button("Add", variant="primary", id="add-btn")
    
    def on_button_pressed(self, event: Button.Pressed):

        if event.button.id == "add-btn":
            title = self.query_one("#title-input", Input)
            desc = self.query_one("#desc-input", Input)
            # Emit message to parent app to handle adding
            self.post_message(self.AddTask(title.value, desc.value))
            title.value = ""
            desc.value = ""

class AddTask(Message):

    def __init__(self, title: str, description: str):
        super().__init__()
        self.title = title
        self.description = description


    