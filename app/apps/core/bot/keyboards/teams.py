from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def teams_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='👥 Команда Стаса', callback_data='team_1'),
         InlineKeyboardButton(text='👥 Команда Артёма', callback_data='team_2')],

    ])