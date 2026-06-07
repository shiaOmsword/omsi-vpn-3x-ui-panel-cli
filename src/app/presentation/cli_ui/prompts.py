from __future__ import annotations

from typing import Any

from rich.prompt import Prompt, IntPrompt, Confirm
from app.common.console.console import console
from .registry import run_action
from app.common.utils.tools import validate_not_empty



def ask_params(command: dict[str, Any]) -> dict[str, Any]:
    result = {}

    for param in command.get("params", []):
        name = param["name"]
        prompt_text = param.get("prompt", name)
        param_type = param.get("type", "str")
        default = param.get("default", None)

        if param_type == "int":
            value = IntPrompt.ask(prompt_text, default=default)
        elif param_type == "bool":
            value = Confirm.ask(prompt_text, default=bool(default))
        else:
            value = Prompt.ask(prompt_text, default=default)

        result[name] = value

    return result


async def handle_command(command: dict[str, Any]) -> bool:
    action = command.get("action")

    if not action:
        console.print("[red]У команды не указан action[/red]")
        return True

    params = ask_params(command)

    if command.get("confirm", False):
        confirm_text = command.get("confirm_text", "Подтвердить действие?")
        confirmed = Confirm.ask(confirm_text)

        if not confirmed:
            console.print("[yellow]Действие отменено[/yellow]")
            return True

    return await run_action(action, params)