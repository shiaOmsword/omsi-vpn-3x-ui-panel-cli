
from pathlib import Path
import typer

from app.common.utils.config_loader import load_config
from app.common.utils.tools import find_command_by_key
from app.presentation.cli_ui.menu import render_header, render_menu, console
from app.presentation.cli_ui.prompts import handle_command
from rich.prompt import Prompt
from app.bootstrap.cli_actions.app import app
import asyncio

@app.command()
def get_users(
    config_path: Path = typer.Option(
        Path("config/local.yml"),
        "--config",
        "-c",
        help="Путь к YAML-конфигу",
    )
) -> None:
    asyncio.run(get_users_async(config_path))


async def get_users_async(config_path: Path) -> None:
    config = load_config(config_path)
    render_header(config)
    await handle_command("get_users")