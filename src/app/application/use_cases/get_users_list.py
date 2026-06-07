from app.application.ports import PanelPort
from app.application.dto import UserDTO
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

def map_dict_to_dto(user:dict)->UserDTO:
    return UserDTO(
        id=user.get("id", "-"),
        email=user["email"],
        sub_id=user["subId"],
        enable=user["enable"],
        flow=user["flow"],
        created_at=parse_timestamp(user["createdAt"]),
        updated_at=parse_timestamp(user["updatedAt"]),
        inboundIds=user["inboundIds"],
    )

def parse_timestamp(value:int, user_tz:str = "Europe/Moscow") -> datetime:
    dt = datetime.fromtimestamp(
        value/1000,
        tz=timezone.utc,
    ).astimezone(ZoneInfo(user_tz))
    return dt.strftime("%y-%m-%d %H:%M:%S")

class GetUsersListUseCase:
    def __init__(
        self,
        panel: PanelPort,
    ):
        self.panel = panel
    
    async def execute(self)->list[UserDTO]:
        users = await self.panel.get_users()
        #print(users.get("obj"))
        
        return [map_dict_to_dto(user) for user in users.get("obj")]