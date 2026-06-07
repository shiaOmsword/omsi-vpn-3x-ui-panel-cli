from app.application.ports import PanelPort
from app.application.dto import UserDTO
from app.common.errors.exceptions import ApiClientError

class CreateUserUseCase:
    def __init__(
        self,
        panel: PanelPort,
    ):
        self.panel = panel
    
    async def execute(self, payload:dict|None = None)->UserDTO:
        if payload is None:
            raise ApiClientError("Payload is empty, plese fill data")
        
        response = await self.panel.create_client(payload=payload)
        
        if not response.get("success"):
            raise ApiClientError(f"Client was not created: {response}")
        
        # for attempt in range(3):
        #     print(f"try to get new user attempt {attempt}/3...")
            
        #     user = await self.panel.get_user(email)
        #     if user.get("obj") is not None:
        #         return user            

        #     await asyncio.sleep(5)
            
        # raise ApiClientError(f"User was created, but was not found by email={email}")