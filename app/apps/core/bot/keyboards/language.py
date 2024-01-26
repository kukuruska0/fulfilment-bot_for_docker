from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def language_ikb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='RUS 🇷🇺', callback_data='ru'),
         InlineKeyboardButton(text='ENG 🇬🇧', callback_data='en')]
    ])
