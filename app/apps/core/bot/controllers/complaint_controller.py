from app.apps.core.bot.helpers import messager
from app.apps.core.bot.services.can_response import CanResponse
from app.apps.core.bot.services.has_iogram_entities import HasIogramEntites


class ComplaintController(HasIogramEntites, CanResponse):

    async def show_complaint_message(self):
        await self.response(messager('complaint'))
