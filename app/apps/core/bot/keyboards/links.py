from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def links_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Перейти на сайт', url='https://fulfillmentmoscow.ru/'),
         InlineKeyboardButton(text='Перейти в чат', url='https://t.me/+7BXfUVG5TvAzZTIy')],
        [InlineKeyboardButton(text='Инстаграм', url='https://instagram.com/fulfilment_saxar'),
         InlineKeyboardButton(text='VK', url='https://vk.com/fulfillment_moskva')]

    ])