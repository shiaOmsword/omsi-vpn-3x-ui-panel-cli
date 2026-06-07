from app.common.console.console import console
from rich.panel import Panel
from dataclasses import dataclass

@dataclass
class BlockPanel:
    message:str
    title:str
    text_colour:str
    panel_border_colour:str
    
    def build_panel(self)->Panel:
        return Panel(
            self.message,
            title=self.title, 
            style=self.text_colour,
            border_style=self.panel_border_colour,
        )