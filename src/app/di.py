from app.config.settings import get_settings
from app.infrastructure.http.base_client import ApiClient
from app.infrastructure.control_panel.gateway import ControlPanelGateway
from typing import Any
from app.application.use_cases.get_users_list import GetUsersListUseCase
from app.application.use_cases.create_client import CreateUserUseCase
from app.application.use_cases.get_user import GetUserUseCase

from app.application.facades.panel_facade import PanelFacade
from app.application.facades.app_facade import AppFacade

class AppContainer:
    def __init__(self):
        self.settings = get_settings()
        self.client: ApiClient | None = None
        

    async def __aenter__(self) -> "AppContainer":
        self.client = ApiClient(
            base_url=self.settings.base_url,
            token=self.settings.panel_token,
        )

        await self.client.open()
        return self
    
    async def __aexit__(self, exc_type, exc, tb) -> None:
        if self.client is not None:
            await self.client.close()
        

    def get_control_panel_gateway(self) -> ControlPanelGateway:
        if self.client is None:
            raise RuntimeError("ApiClient is not initialized. Use async with AppContainer().")

        return ControlPanelGateway(client=self.client)
        
    def get_users_list_use_case(self) -> GetUsersListUseCase:
        panel = self.get_control_panel_gateway()
        return GetUsersListUseCase(panel=panel)
    
    def get_create_user_use_case(self) -> CreateUserUseCase:
        panel = self.get_control_panel_gateway()
        return CreateUserUseCase(panel=panel)
    
    def get_get_user_use_case(self) -> GetUserUseCase:
        panel = self.get_control_panel_gateway()
        return GetUserUseCase(panel=panel)
    
    def get_panel_facade(self) -> PanelFacade:
        return PanelFacade(
            get_users_list_use_case=self.get_users_list_use_case(),
            get_create_user_use_case=self.get_create_user_use_case(),
            get_get_user_use_case=self.get_get_user_use_case(),
        )
        

    def app(self) -> AppFacade:
        return AppFacade(
            panel=self.get_panel_facade(),
        )    
        
        
        