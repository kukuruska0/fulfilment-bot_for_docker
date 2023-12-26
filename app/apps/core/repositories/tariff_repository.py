from tarfile import TarInfo
from typing import Final
from asgiref.sync import sync_to_async
from app.apps.core.models import TariffPlan, TelegramUser
from app.apps.core.repositories.user_repository import UserRepository
from app.apps.core.DTO import TariffDto
from app.apps.core.repositories.base import BaseRepository


class TariffRepository(BaseRepository):
    model = TariffPlan
    

    @sync_to_async
    def get_default(self) -> TariffPlan:
        return self.model.objects.filter(is_default=True).first()

    @sync_to_async
    def attach_default_to_user(self, user: TelegramUser) -> TariffPlan:
        try:
            default = self.model.objects.filter(is_default=True).first()
            user.tariff_plan = default
            user.save()
            return True
        except Exception:
            return False

    @sync_to_async
    def is_permited_for_user(self, user_id, key):
        user = self.model.objects.filter(telegram_id=user_id).first()
        if (user and user.tariff_plan):
            tariff = TariffDto(user.tariff_plan)
            return int(tariff.__dict__[key])
        else:
            return None
        
        
    @sync_to_async
    def get_by_user(self, user: TelegramUser, **args):
        query = self.model.objects.filter(user=user)

        if (args):
            query = query.filter(**args)

        return super().to_list(query.all())       
        

