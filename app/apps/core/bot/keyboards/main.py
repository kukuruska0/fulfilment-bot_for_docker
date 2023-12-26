from aiogram.types import InlineKeyboardMarkup
from app.apps.core.bot.keyboards.buttons import make_inline_btn
from aiogram.utils.keyboard import *
from aiogram.types import *
from app.apps.core.bot.filters import UserCallbackData

def hello():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            make_inline_btn(
                    transl_text='buttons.say_hello',
                    # action='search_status',
                    # callback_data=UserCallbackData,
                    # id=user_id,
                    # chat_id=chat_id,
                    # search_id=search_id,
                    # message_id=search_msg_id
                    
            )
        ]
    ])
    
    
def force_reply(placeholder: str | None = None):
    return ForceReply(input_field_placeholder=placeholder)