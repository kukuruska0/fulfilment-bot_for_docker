from aiogram import F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import *
from aiogram.utils.formatting import Bold, Text
from aiogram.utils.i18n import gettext as _

from app.apps.core.bot.controllers.address_controller import AddressController
from app.apps.core.bot.controllers.calculation_controller import CalculationController
from app.apps.core.bot.controllers.complaint_controller import ComplaintController
from app.apps.core.bot.controllers.links_controller import LinksController
from app.apps.core.bot.controllers.main_controller import MainController
from app.apps.core.bot.controllers.price_controller import PriceController
from app.apps.core.bot.controllers.product_controller import ProductController
from app.apps.core.bot.controllers.shipment_controller import ShipmentController
from app.apps.core.bot.controllers.spoilage_controller import SpoilageController
from app.apps.core.bot.keyboards.main import start_kb
from app.apps.core.bot.services.router import Router
from app.apps.core.bot.states import GetLanguage
from app.services.i18n_translater import i18n_middleware

router = Router()

# TODO Make for other iogram  events (done only for message action )
router.action_message(MainController, MainController.action_start, Command(commands=["start"]))
router.action_message(CalculationController, CalculationController.show_calculation_message, F.text == '📑 Calculate')
router.action_message(CalculationController, CalculationController.show_calculation_message, F.text == '📑 Расчёт')
router.action_message(ProductController, ProductController.show_product_message, F.text == '📦 Забор товара')
router.action_message(ProductController, ProductController.show_product_message, F.text == '📦 Picking up goods')
router.action_message(PriceController, PriceController.show_price_message, F.text == '📈 Прайс')
router.action_message(PriceController, PriceController.show_price_message, F.text == '📈 Price')
router.action_message(ShipmentController, ShipmentController.show_shipment_message, F.text == '🚚 Отгрузка')
router.action_message(ShipmentController, ShipmentController.show_shipment_message, F.text == '🚚 Shipment')
router.action_message(AddressController, AddressController.show_address_message, F.text == '📍 Адрес')
router.action_message(AddressController, AddressController.show_address_message, F.text == '📍 Address')
router.action_message(SpoilageController, SpoilageController.show_spoilage_message, F.text == '🚫 Брак')
router.action_message(SpoilageController, SpoilageController.show_spoilage_message, F.text == '🚫 Spoilage')
router.action_message(ComplaintController, ComplaintController.show_complaint_message, F.text == '❓ Рекламации')
router.action_message(ComplaintController, ComplaintController.show_complaint_message, F.text == '❓ Complaints')
router.action_message(LinksController, LinksController.show_links, F.text == '🔗 Ссылки')
router.action_message(LinksController, LinksController.show_links, F.text == '🔗 Links')


@router.message(F.text == '🛠 Тех задание')
async def technical_task(message: Message):
    content = Text(Bold(_('Напишите мне, я помогу Вам с расчётом:\nhttps://t.me/EkaterinaLevchenko')))
    await message.answer(**content.as_kwargs())
    await message.answer('https://docs.google.com/spreadsheets/d/1aKHtu2WfY9QIylXH2fVzanB4fYwdn8y8/edit?usp=drive_link&ouid=110660432788308438181&rtpof=true&sd=true')
    await message.answer('https://docs.google.com/spreadsheets/d/1-CL8bwQWQxSas0dZ2Uzb8W-7Do9Hx8HL/edit?usp=drive_link&ouid=110660432788308438181&rtpof=true&sd=true')


@router.message(F.text == '🛠 Technical task')
async def technical_task(message: Message):
    content = Text(Bold(_('Напишите мне, я помогу Вам с расчётом:\nhttps://t.me/EkaterinaLevchenko')))
    await message.answer(**content.as_kwargs())
    await message.answer('https://docs.google.com/spreadsheets/d/1aKHtu2WfY9QIylXH2fVzanB4fYwdn8y8/edit?usp=drive_link&ouid=110660432788308438181&rtpof=true&sd=true')
    await message.answer('https://docs.google.com/spreadsheets/d/1-CL8bwQWQxSas0dZ2Uzb8W-7Do9Hx8HL/edit?usp=drive_link&ouid=110660432788308438181&rtpof=true&sd=true')


@router.message(F.text == '📝 Договор')
async def agreement(message: Message):
    await message.answer('https://docs.google.com/document/d/1Tr6K-ZCZOaWlEhypFfsQlwFHks105fnf/edit?usp=drive_link&ouid=110660432788308438181&rtpof=true&sd=true')


@router.message(F.text == '📝 Contract')
async def agreement(message: Message):
    await message.answer('https://docs.google.com/document/d/1Tr6K-ZCZOaWlEhypFfsQlwFHks105fnf/edit?usp=drive_link&ouid=110660432788308438181&rtpof=true&sd=true')


@router.callback_query(F.data == 'team_1')
async def team_1(callback: CallbackQuery):
    content = Text(Bold(_('Конакты команды Стаса:\nhttps://t.me/saxargroupFf')))
    await callback.message.answer(**content.as_kwargs())
    await callback.answer()


@router.callback_query(F.data == 'team_2')
async def team_2(callback: CallbackQuery):
    content = Text(Bold(_('Конакты команды Артема:\nhttps://t.me/SAXAR_GROUP_team_Artem')))
    await callback.message.answer(**content.as_kwargs())
    await callback.answer()


@router.callback_query(F.data == 'ru')
async def language_ru(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(GetLanguage.get_language)
    await i18n_middleware.set_locale(state=state, locale=callback.data)
    content = Text(Bold(_('Здравствуйте!\n\nВыберите нужный пункт')))
    content2 = Text(Bold(_('Язык выбран') + ' 🇷🇺'))
    await callback.message.answer(**content2.as_kwargs(), reply_markup=ReplyKeyboardRemove())
    await callback.message.answer(**content.as_kwargs(), reply_markup=start_kb())


@router.callback_query(F.data == 'en')
async def language_ru(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(GetLanguage.get_language)
    await i18n_middleware.set_locale(state=state, locale=callback.data)
    content = Text(Bold(_('Здравствуйте!\n\nВыберите нужный пункт')))
    content2 = Text(Bold(_('Язык выбран') + ' 🇬🇧'))
    await callback.message.answer(**content2.as_kwargs(), reply_markup=ReplyKeyboardRemove())
    await callback.message.answer(**content.as_kwargs(), reply_markup=start_kb())
