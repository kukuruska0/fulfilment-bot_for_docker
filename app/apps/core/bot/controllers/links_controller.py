from app.apps.core.bot.helpers import messager
from app.apps.core.bot.keyboards.links import links_kb
from app.apps.core.bot.services.can_response import CanResponse
from app.apps.core.bot.services.has_iogram_entities import HasIogramEntites


class LinksController(HasIogramEntites, CanResponse):

    async def show_links(self):
        await self.response(messager('links'), reply_markup=links_kb())
