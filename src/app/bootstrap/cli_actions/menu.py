
from pathlib import Path
import typer

from app.common.utils.config_loader import load_config
from app.common.utils.tools import find_command_by_key
from app.presentation.cli_ui.menu import render_header, render_menu
from app.presentation.cli_ui.prompts import handle_command
from rich.prompt import Prompt
from app.common.console.console import console
from app.bootstrap.cli_actions.app import app
import asyncio

@app.command()
def menu(
    config_path: Path = typer.Option(
        Path("config/local.yml"),
        "--config",
        "-c",
        help="Путь к YAML-конфигу",
    )
) -> None:
    asyncio.run(menu_async(config_path))


async def menu_async(config_path: Path) -> None:
    try:
        config = load_config(config_path)
    except Exception as error:
        console.print(f"[red]Ошибка загрузки конфига:[/red] {error}")
        raise typer.Exit(code=1)

    render_header(config)

    while True:
        render_menu(config)

        choice = Prompt.ask("\nВыбери действие")
        command = find_command_by_key(config, choice)

        if command is None:
            console.print("[red]Такой команды нет[/red]")
            continue

        should_continue = await handle_command(command)

        if not should_continue:
            break

        console.print()
        Prompt.ask("[dim]Нажми Enter, чтобы вернуться в меню[/dim]", default="")