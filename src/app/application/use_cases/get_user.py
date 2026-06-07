from app.application.ports import PanelPort
from app.application.dto import UserDTO
from app.common.errors.exceptions import ApiClientError
from .get_users_list import parse_timestamp

def map_dict_to_user_dto(data:dict)->UserDTO:
    client = data.get("client")
    inbounds = data.get("inboundIds")
    return UserDTO(
        id=client.get("id", "-"),
        email=client["email"],
        sub_id=client["subId"],
        enable=client["enable"],
        flow=client["flow"],
        created_at=parse_timestamp(client["createdAt"]),
        updated_at=parse_timestamp(client["updatedAt"]),
        inboundIds=inbounds,
    )

class GetUserUseCase:
    def __init__(
        self,
        panel: PanelPort,
    ):
        self.panel = panel
    
    async def execute(self, email:str)->UserDTO:
        if dict is None:
            raise ApiClientError("Data is empty, plese fill data for search user")
        
        user = await self.panel.get_user(email=email)
        
        return map_dict_to_user_dto(user.get("obj"))