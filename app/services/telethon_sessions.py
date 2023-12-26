

from telethon import TelegramClient
from app.apps.core.DTO import SearchTelegramAccount
import asyncio

#TODO 
# https://docs.telethon.dev/en/stable/developing/test-servers.html
async def init_and_start():
    username = ''
    api_id = ''
    api_hash = ''
    phone = ''
    client =  TelegramClient(username, int(api_id), api_hash, system_version="4.16.30-vxCUSTOM") 
    await client.start(phone=phone)
    return client



    
# Iterations Untill disconnect
def telegram_daemon():
    def wrapper(func):
        async def wrapped(obj, **args):
            client:TelegramClient = await init_and_start()
            await func(self=obj, client=client, **args)
            await client.run_until_disconnected()
        return wrapped
    return wrapper
    


# One iteration
def telegram_iteration():
    def wrapper(func):
        async def wrapped(obj, **args):
            client:TelegramClient = await init_and_start()
            await func(self=obj, client=client, **args)
            await client.disconnect()
        return wrapped
    return wrapper


