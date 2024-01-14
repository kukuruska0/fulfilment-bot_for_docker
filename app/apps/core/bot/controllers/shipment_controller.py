from app.apps.core.bot.helpers import messager
from app.apps.core.bot.keyboards.teams import teams_kb
from app.apps.core.bot.services.can_response import CanResponse
from app.apps.core.bot.services.has_iogram_entities import HasIogramEntites


class ShipmentController(HasIogramEntites, CanResponse):

    async def show_shipment_message(self):
        await self.response(messager('shipment'), reply_markup=teams_kb())
