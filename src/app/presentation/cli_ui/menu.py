from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich import box
from typing import Any
from app.common.console.console import console

def render_header(config: dict[str, Any]) -> None:
    app_config = config.get("app", {})

    title = app_config.get("title", "CLI App")
    subtitle = app_config.get("subtitle", "")

    console.print(
        Panel.fit(
            f"[bold cyan]{title}[/bold cyan]\n[dim]{subtitle}[/dim]",
            border_style="cyan",
        )
    )
    
def render_menu(config: dict[str, Any]) -> None:
    screen = config.get("screens", {}).get("main_menu", {})
    commands = config.get("commands", [])

    title = screen.get("title", "Меню")
    description = screen.get("description", "")

    console.print(
        Panel(
            f"[bold green]{title}[/bold green]\n[dim]{description}[/dim]\n",
            border_style="green",
        )
    )

    table = Table(
        title="Доступные действия",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold magenta",
    )

    table.add_column("Клавиша", justify="center", style="cyan", no_wrap=True)
    table.add_column("Действие", style="bold")
    table.add_column("Описание", style="dim")

    for command in commands:
        table.add_row(
            str(command.get("key", "")),
            command.get("title", ""),
            command.get("description", ""),
        )

    console.print(table)
    