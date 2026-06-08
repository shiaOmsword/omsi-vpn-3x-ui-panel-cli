from typing import Protocol, Any


class PanelPort(Protocol):
    async def get_user(self, email:str):
        ...
        
    async def get_users(self) -> list[dict[str, Any]]:
        ...

    async def create_client(self, payload: dict[str, Any]) -> dict[str, Any]:
        ...

    async def delete_client(self, params:dict) -> None:
        ...