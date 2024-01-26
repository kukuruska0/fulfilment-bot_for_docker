from app.apps.core.bot.helpers import messager
from app.apps.core.bot.keyboards.language import language_ikb
from app.apps.core.bot.services.can_response import CanResponse
from app.apps.core.bot.services.has_iogram_entities import HasIogramEntites


class MainController(HasIogramEntites, CanResponse):

    async def action_start(self):
        await self.response(messager('start'), reply_markup=language_ikb())
