from __future__ import annotations
from typing import Any
from rich.panel import Panel
from rich.table import Table
from app.common.console.console import console
from app.di import AppContainer
from dataclasses import fields
from app.application.dto import UserDTO
from datetime import datetime
from app.common.utils.tools import parse_datetime, is_created_after, format_inbound_ids, validate_not_empty
from .format import format_users_table
import uuid
from rich.prompt import Prompt, IntPrompt, Confirm
from app.config.settings import get_settings
settings = get_settings()
def create_user_prompt()->dict:
    email = Prompt.ask("[yellow]Введите название ключа или оно будет сгенерировано автоматически[/yellow]")
    inbound_id = IntPrompt.ask("[yellow]Введите номер инбаунда[/yellow]", choices=["1","2"],  default=1)
    
    email=validate_not_empty(email)
    
    console.print(
        f"[red]Имя ключа:[/red]{email}\n"
        f"[red]Номер подключения:[/red]{inbound_id}"
    )
    
    data:dict[str, Any] = {
        "client": {
            "email":email,
            "group":"work_1",
            "enable": True,
            "flow":"xtls-rprx-vision",
            "expiryTime": 0,
            "totalGB": 0,
        },
        "inboundIds":[inbound_id]
    }
    
    return data, email
HEADERS_ROW = [
    "id",
    "email",
    "sub_id",
    "enable",
    "flow",
    "created_at",
    "updated_at",
    "inbound_ids",
]

async def status_handler(params: dict[str, Any]) -> bool:
    console.print(Panel("[green]Система работает нормально[/green]", title="Статус"))
    return True

async def create_user(params: dict[str, Any]) -> bool:
    console.print(Panel("[green] Создание ключа VPN для пользователя[/green]", title="Creating VPN key"))
    data, email = create_user_prompt()
    
    async with AppContainer() as container:
        app = container.app()
        user = await app.panel.create_user(payload=data)
        user = await app.panel.get_user(email=email)
    #print(user)
    console.print(f"[green]Пользователь создан[/green]:\n Ссылка на подписку:{settings.base_url_sub}{user.sub_id}")
    return True

async def get_users_handler(params: dict[str, Any]) -> bool:
    console.print("[yellow]Загружаю пользователей...[/yellow]")
    table = Table(title="Пользователи")
    format_users_table(HEADERS_ROW, table)
    
    async with AppContainer() as container:
        app = container.app()
        users = await app.panel.get_users()
    
    date_from = datetime.strptime("26-06-01 00:00:00", "%y-%m-%d %H:%M:%S")
    users_june:list[UserDTO] = list(filter(lambda user: is_created_after(user, date_from), sorted(users, key=lambda item: item.created_at)))
    
    for user in users:
        table.add_row(
            str(user.id),
            user.email,
            user.sub_id,
            str(user.enable),
            user.flow,
            user.created_at,
            user.updated_at,
            format_inbound_ids(user.inboundIds),
        )
        
    console.print(table)
    return True


async def quit_handler(params: dict[str, Any]) -> bool:
    console.print("[cyan]Выход из программы[/cyan]")
    return False