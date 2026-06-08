from app.application.use_cases.get_users_list import GetUsersListUseCase
from app.application.use_cases.create_client import CreateUserUseCase
from app.application.use_cases.get_user import GetUserUseCase
from app.application.use_cases.delete_user import DeleteUserUseCase
class PanelFacade:
    def __init__(
        self,
        get_users_list_use_case: GetUsersListUseCase,
        get_create_user_use_case: CreateUserUseCase,
        get_get_user_use_case: GetUserUseCase,
        get_delete_user_use_case: DeleteUserUseCase,
    ) -> None:
        self._get_users_list_use_case = get_users_list_use_case
        self._get_create_user_use_case = get_create_user_use_case
        self._get_get_user_use_case = get_get_user_use_case
        self._get_delete_user_use_case = get_delete_user_use_case
    
    async def get_user(self, email:str):
        return await self._get_get_user_use_case.execute(email=email)

    async def get_users(self):
        return await self._get_users_list_use_case.execute()
    
    async def create_user(self, payload:dict):
        return await self._get_create_user_use_case.execute(payload=payload)
    
    async def delete_user(self, params:dict):
        return await self._get_delete_user_use_case.execute(params=params)