import aiogram.types.inline_keyboard_markup
from aiogram.utils.keyboard import *
from aiogram.types import *
from app.apps.core.bot.filters import UserCallbackData
from app.services.translater import t as transl
import json


def change_tariff_btn(user_id, tariff_id=None, msg_id: Message = None, action_type='expired'):
    return make_inline_btn('buttons.tariff.change',
                           action='buy_tariff',
                           id=user_id,
                           tariff_id=tariff_id,
                           message_id=msg_id,
                           type=action_type)


def make_inline_btn(
        transl_text,
        action: str | None = None,
        callback_data=UserCallbackData,
        **args
):
    if action:
        callback_data = callback_data(**(args | {'action': action})).pack()
    else:
        callback_data = None

    return InlineKeyboardButton(text=transl(transl_text), callback_data=callback_data)


def clear_btn(btn_text='buttons.clear', **args):
    return make_inline_btn(btn_text, **args)


def save_btn(btn_text='buttons.save', **args):
    return make_inline_btn(btn_text, **args)


def request_chat_btn(id, btn_text='buttons.bot.add_chat'):
    return KeyboardButton(
        text=transl(btn_text),
        request_chat=KeyboardButtonRequestChat(
            request_id=id, chat_is_channel=False)
    )


def request_poll_btn(btn_text='buttons.bot.add_words', type='regular'):
    return KeyboardButton(
        text=transl(btn_text),
        request_poll=KeyboardButtonPollType(type=type)
    )
