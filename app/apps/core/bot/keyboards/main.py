from aiogram.types import *

from app.messages.ru.commands import *


def start_kb():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=cmd_calculate), KeyboardButton(text=cmd_technical_task)],
        [KeyboardButton(text=cmd_product), KeyboardButton(text=cmd_address)],
        [KeyboardButton(text=cmd_price), KeyboardButton(text=cmd_agreement)],
        [KeyboardButton(text=cmd_shipment), KeyboardButton(text=cmd_spoilage)],
        [KeyboardButton(text=cmd_complaints)],
        [KeyboardButton(text=cmd_links)]

    ])


def force_reply(placeholder: str | None = None):
    return ForceReply(input_field_placeholder=placeholder)
