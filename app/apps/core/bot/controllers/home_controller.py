from aiogram import Router
from aiogram.filters import Command
from app.apps.core.bot.services.can_response import CanResponse
from app.config.application import INSTALLED_APPS
from aiogram import F
from typing import *
from aiogram.types import *
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, BotCommand
from app.apps.core.repositories.user_repository import UserRepository
from aiogram import Bot, Router, types, F
from sqlalchemy.ext.asyncio import AsyncSession
from app.apps.core.bot.services.has_iogram_entities import HasIogramEntites
from app.apps.core.bot.helpers import messager
from app.apps.core.bot.keyboards.main import hello


class HomeController(HasIogramEntites, CanResponse):
    
    async def action_hello(self):
        await self.response(messager('hello'), reply_markup=hello())