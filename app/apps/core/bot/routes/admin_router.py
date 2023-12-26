from app.apps.core.bot.controllers.admin.home_controller import HomeController
from app.apps.core.bot.services.router import Router
from aiogram.filters import Command
from typing import *
from aiogram.types import *
from aiogram.fsm.context import FSMContext
from aiogram.utils.formatting import *

router = Router()


#TODO Make for other iogram  events (done only for message action )
router.action_message( HomeController, HomeController.action_hello, Command(commands=["start"]))








