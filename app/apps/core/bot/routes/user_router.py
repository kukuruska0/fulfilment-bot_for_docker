from aiogram import F
from aiogram.filters import Command
from aiogram.types import *

from app.apps.core.bot.controllers.address_controller import AddressController
from app.apps.core.bot.controllers.calculation_controller import CalculationController
from app.apps.core.bot.controllers.complaint_controller import ComplaintController
from app.apps.core.bot.controllers.links_controller import LinksController
from app.apps.core.bot.controllers.main_controller import MainController
from app.apps.core.bot.controllers.price_controller import PriceController
from app.apps.core.bot.controllers.product_controller import ProductController
from app.apps.core.bot.controllers.shipment_controller import ShipmentController
from app.apps.core.bot.controllers.spoilage_controller import SpoilageController
from app.apps.core.bot.services.router import Router
from app.messages.ru.commands import *
from app.messages.ru.message_text import *

router = Router()

# TODO Make for other iogram  events (done only for message action )
router.action_message(MainController, MainController.action_start, Command(commands=["start"]))
router.action_message(CalculationController, CalculationController.show_calculation_message, F.text == cmd_calculate)
router.action_message(ProductController, ProductController.show_product_message, F.text == cmd_product)
router.action_message(PriceController, PriceController.show_price_message, F.text == cmd_price)
router.action_message(ShipmentController, ShipmentController.show_shipment_message, F.text == cmd_shipment)
router.action_message(AddressController, AddressController.show_address_message, F.text == cmd_address)
router.action_message(SpoilageController, SpoilageController.show_spoilage_message, F.text == cmd_spoilage)
router.action_message(ComplaintController, ComplaintController.show_complaint_message, F.text == cmd_complaints)
router.action_message(LinksController, LinksController.show_links, F.text == cmd_links)


@router.message(F.text == cmd_technical_task)
async def technical_task(message: Message):
    await message.answer(cmd_technical_task_text)
    await message.answer_document(FSInputFile(path=r'D:\\Pictures\\ТЗ_OZON_ВАША_ФАМИЛИЯ_ДАТА_ОТПРАВКИ_ТЗ.xlsx'))
    await message.answer_document(FSInputFile(path=r'D:\\Pictures\\ТЗ_ВАША ФАМИЛИЯ_ДАТА ОТПРАВКИ ТЗ.xlsx'))


@router.message(F.text == cmd_agreement)
async def agreement(message: Message):
    await message.answer_document(FSInputFile(path=r'D:\\Pictures\\Contract_SAXARGROUP.docx'))


@router.callback_query(F.data == 'team_1')
async def team_1(callback: CallbackQuery):
    await callback.message.answer('Конакты команды Стаса:\nhttps://t.me/saxargroupFf')
    await callback.answer()


@router.callback_query(F.data == 'team_2')
async def team_2(callback: CallbackQuery):
    await callback.message.answer('Конакты команды Артема:\nhttps://t.me/SAXAR_GROUP_team_Artem')
    await callback.answer()
