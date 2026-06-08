from app.infrastructure.http.base_client import ApiClient

class ControlPanelGateway:
    def __init__(
        self,
        client: ApiClient,
    )-> None:
        self.client = client
        
    async def get_user(self, email:str):
        return await self.client.get(f"/panel/api/clients/get/{email}")
    
    async def get_users(self)->list[dict]:
        return await self.client.get("/panel/api/clients/list")
    
    async def create_client(self,payload:dict):
        return await self.client.post("/panel/api/clients/add", json=payload)
        
    async def delete_client(self, params:dict):
        return await self.client.post(f"/panel/api/clients/del/{params.get("email")}", params={"keepTraffic":0})