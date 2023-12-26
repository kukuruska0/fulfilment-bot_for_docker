from app.apps.core.DTO import SearchTelegramAccount

from telethon import utils, TelegramClient

from app.services.telethon_sessions import telegram_daemon, telegram_iteration
from telethon import functions, types
from telethon.tl.types import PeerUser, PeerChat, PeerChannel


class TelegramWalker:
        
    def __init__(self) -> None:
       pass
        
    @telegram_iteration()
    async def subscribe_to_chat(self):
        pass 


