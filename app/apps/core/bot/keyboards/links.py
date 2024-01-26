from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.i18n import gettext as _


def links_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=_('Перейти на сайт'), url='https://fulfillmentmoscow.ru/'),
         InlineKeyboardButton(text=_('Перейти в чат'), url='https://t.me/+7BXfUVG5TvAzZTIy')],
        [InlineKeyboardButton(text='Instagram', url='https://instagram.com/fulfilment_saxar'),
         InlineKeyboardButton(text='VK', url='https://vk.com/fulfillment_moskva')]

    ])