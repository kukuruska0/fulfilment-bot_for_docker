from aiogram.types import *

from aiogram.utils.i18n import gettext as _


def start_kb():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='📑 ' + _('Расчёт')), KeyboardButton(text='🛠 ' + _('Тех задание'))],
        [KeyboardButton(text='📦 ' + _('Забор товара')), KeyboardButton(text='📍 ' + _('Адрес'))],
        [KeyboardButton(text='📈 ' + _('Прайс')), KeyboardButton(text='📝 ' + _('Договор'))],
        [KeyboardButton(text='🚚 ' + _('Отгрузка')), KeyboardButton(text='🚫 ' + _('Брак'))],
        [KeyboardButton(text='❓ ' + _('Рекламации'))],
        [KeyboardButton(text='🔗 ' + _('Ссылки'))]

    ])


def force_reply(placeholder: str | None = None):
    return ForceReply(input_field_placeholder=placeholder)
