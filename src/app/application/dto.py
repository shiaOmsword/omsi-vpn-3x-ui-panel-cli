from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserDTO:
    email: str | None
    sub_id: str | None
    enable: bool | None
    flow: str | None
    created_at: datetime | None
    updated_at: datetime | None
    inboundIds: list[int] | None
    id: str | None = None