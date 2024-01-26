from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.i18n import gettext as _


def teams_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='👥 ' + _('Команда Стаса'), callback_data='team_1'),
         InlineKeyboardButton(text='👥 ' + _('Команда Артёма'), callback_data='team_2')],

    ])