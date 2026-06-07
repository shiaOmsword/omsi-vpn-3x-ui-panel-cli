import logging
import asyncio
from app.config.settings import get_settings
from app.common.logging.logger import setup_logging
from app.common.console.console import console
from app.common.ui.builders.main_screen import build_main_menu_screen

from app.di import AppContainer

setup_logging()
log = logging.getLogger(__name__)

async def main()->None:
    settings = get_settings()
    
    log.info(f"ping ok | env:{settings.environment}\n")
    console.print(build_main_menu_screen())
    
    async with AppContainer() as container:
        app = container.app()
        users = await app.panel.get_users()
    
    console.print(users)

def cli() -> None:
    asyncio.run(main())