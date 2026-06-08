from typing import Any, Awaitable, Callable
from .handlers import status_handler, get_users_handler, quit_handler, create_user, delete_user_handler
from app.common.console.console import console

Handler = Callable[[dict[str, Any]], Awaitable[bool]]

ACTION_REGISTRY: dict[str, Handler] = {
    "status": status_handler,
    "get_users": get_users_handler,
    "create_user": create_user,
    "delete_user": delete_user_handler,
    "quit": quit_handler,
}


async def run_action(action: str, params: dict[str, Any]) -> bool:
    handler = ACTION_REGISTRY.get(action)

    if handler is None:
        console.print(f"[red]Handler для action='{action}' не найден[/red]")
        return True

    return await handler(params)