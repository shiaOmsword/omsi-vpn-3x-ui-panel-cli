import asyncio
import httpx
from app.common.errors.exceptions import ApiClientError

class ApiClient:
    def __init__(self, token:str, base_url:str):
        self._token = token
        self._base_url = base_url
        self._client: httpx.AsyncClient | None = None
        
    async def open(self) -> None:
        self._client = httpx.AsyncClient(
            base_url=self._base_url,
            headers={
                "Authorization": f"Bearer {self._token}",
                "Accept": "application/json",
            },
            timeout=httpx.Timeout(
                connect=10.0,
                read=30.0,
                write=30.0,
                pool=10.0,
            ),
            follow_redirects=True,
            trust_env=False,
        )
    
    async def close(self)-> None:
        if self._client is not None:
            await self._client.aclose()
            self._client = None
        
    @property
    def client(self) -> httpx.AsyncClient:
        if self._client is None:
            raise RuntimeError("HTTP client is not initialized. Use async with.")
        return self._client
    
    async def _request(
        self,
        method:str,
        path:str,
        **kwargs,
    ) -> dict :
        try:
            response = await self.client.request(
                method=method,
                url=path,
                **kwargs,
            )
            response.raise_for_status()
            
            if response.status_code == 204:
                return None
            
            return response.json()
        
        except httpx.HTTPStatusError as e:
            raise ApiClientError(
                    f"API error {e.response.status_code}: {e.response.text}"
            ) from e
        
        except httpx.RequestError as e:
            raise ApiClientError(f"Network error: {e}") from e
        
    async def get(self, url:str, **kwargs):
        return await self._request("GET", url, **kwargs)
    async def post(self, url:str, **kwargs):
        return await self._request("POST", url, **kwargs)
    async def put(self, url:str, **kwargs):
        return await self._request("PUT", url, **kwargs)
    async def delete(self, url:str, **kwargs):
        return await self._request("DELETE", url, **kwargs)            