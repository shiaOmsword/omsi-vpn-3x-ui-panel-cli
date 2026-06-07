from typing import Any
from rich.panel import Panel
from rich.table import Table
from app.common.console.console import console
from app.di import AppContainer
from dataclasses import fields
from app.application.dto import UserDTO
from datetime import datetime
import uuid

def find_command_by_key(config: dict[str, Any], key: str) -> dict[str, Any] | None:
    commands = config.get("commands", [])

    for command in commands:
        if str(command.get("key")) == key:
            return command

    return 

def parse_datetime(value:str) -> datetime:
    return datetime.strptime(value, "%y-%m-%d %H:%M:%S")

def is_created_after(user:UserDTO, date_from:datetime) -> bool:
    return parse_datetime(user.created_at) >= date_from

def format_inbound_ids(inbound_ids: list[int]) -> str:
    if not inbound_ids:
        return "—"

    return ", ".join(map(str, inbound_ids))

def validate_not_empty(value: str) -> str:
    value = value.strip()
    
    if not value:
        email=f"user_{uuid.uuid4().hex}"
    else:
        email = value
    return email