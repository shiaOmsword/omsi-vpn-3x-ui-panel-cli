from app.application.ports import PanelPort
from app.common.errors.exceptions import ApiClientError
class DeleteUserUseCase:
    def __init__(self, panel: PanelPort):
        self.panel = panel
    
    
    async def execute(self, params:dict)->dict:
        user = await self.panel.get_user(params.get("email"))
        if user.get("obj") is None:
            raise ApiClientError("User not found")
        response = await self.panel.delete_client(params=params)
        return response