from aiogram.types import Message
from app.apps.core.bot.services.responder import Responder
from app.apps.core.bot.keyboards.main import force_reply
from app.services.redis import Redis
from aiogram.exceptions import TelegramBadRequest
from app.apps.core.bot.helpers import messager
from app.apps.core.bot.services.messager import Messager
from app.apps.core.DTO import SearchDto, TariffDto
from app.services.search_services.telegram_walker import TelegramWalker


class CanResponse:
    message: Message

    async def remove_old_message_from_cache(self, key):
        id = Redis().get(key)

        if id:
            try:
                await self.force_delete_msg(self.message.chat.id, id)
                return True
            except (TelegramBadRequest):
                return False

    def set_old_message_to_cache(self, key, message_id):
        Redis().set(key, message_id)

    def get_mess_key(self):
        return f'user_search:{self.message.from_user.id}-old_mess'

    async def action_exception(self, text, reply_markup=None, **args):
        return await Responder(self.message).answer(Messager.action_exception(text), reply_markup, **args)

    async def response(self, text, reply_markup=None, autodelete_seconds: int | None = None, **args):
        return await Responder(self.message).answer(text, reply_markup, autodelete_seconds=autodelete_seconds, **args)

    async def reply(self, text, reply_markup=None, autodelete_seconds: int | None = None, **args):
        return await Responder(self.message).reply(text, reply_markup, autodelete_seconds=autodelete_seconds, **args)

    async def force_reply(self, text, placeholder: str | None = None, **args):
        return await Responder(self.message).answer(text, reply_markup=force_reply(placeholder), **args)

    async def delete_markup(self, **args):
        return await Responder(self.message).delete_reply_markup(**args)

    async def delete_message(self, message: Message | None = None, **args):
        return await Responder(self.message).delete_msg(message, **args)

    async def force_delete_msg(self, chat_id, msg_id):
        return await Responder(self.message).force_delete(chat_id, msg_id)

    async def edit(self, text, reply_markup=None, message_id: str | None = None, **args):
        return await Responder(self.message).edit(text, inline_message_id=message_id, reply_markup=reply_markup, **args)

    async def change_markup(self, markup, message_id: str | None = None, **args):
        return await Responder(self.message).edit_reply_markup(inline_message_id=message_id, reply_markup=markup,  **args)

  
