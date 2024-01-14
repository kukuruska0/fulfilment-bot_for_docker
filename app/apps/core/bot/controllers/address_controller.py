from app.apps.core.bot.helpers import messager
from app.apps.core.bot.services.can_response import CanResponse
from app.apps.core.bot.services.has_iogram_entities import HasIogramEntites


class AddressController(HasIogramEntites, CanResponse):

    async def show_address_message(self):
        await self.response(messager('address'))
