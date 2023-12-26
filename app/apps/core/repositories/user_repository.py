from typing import Final
from asgiref.sync import sync_to_async, async_to_sync
from app.apps.core.models import TariffPlan, TelegramUser
from aiogram.types import Message
from app.apps.core.DTO import TariffDto


class UserRepository:
    message: Message
    model = TelegramUser
    
    @sync_to_async
    def save_and_set_tariff(self: None, data: dict, tariff: TariffPlan | None = None, get_entities: bool | None = None):
        user = TelegramUser.objects.filter(
            telegram_id=data['telegram_id']).first()

        if (not user):
            user = TelegramUser(telegram_id=data['telegram_id'])
            
        if (not tariff):
            tariff = TariffPlan.objects.filter(is_default=True).first()

        user.telegram_username = data['telegram_username']
        user.telegram_name = data['telegram_name']
        user.tariff_plan = tariff

        try:
            user.save()
            if get_entities:
                return [user, tariff]
            return True
        except Exception:
            return False

    @sync_to_async
    def set_tariff(self: None,  user:TelegramUser, tariff: TariffPlan | None = None, get_entities: bool = False):
        if (not tariff):
            tariff = TariffPlan.objects.filter(is_default=True).first()

        try:
            user.tariff_plan = tariff
            user.save()
            if get_entities:
                return [user, tariff]
            return True
        except Exception:
            return False

    def check_username(name: str) -> bool:
        if isinstance(name, str) and 3 < len(name) < 12 and name[0].isalpha():
            return True
        return False

    @sync_to_async
    def get_tariff(self: None, id: int):
        user = TelegramUser.objects.filter(telegram_id=id).first()
        
        return user.tariff_plan
    
    #TODO Calculate tariff
    @sync_to_async
    def get_permited_tariff(self: None, user_or_id: int|TelegramUser, with_dto=True)-> TariffDto:
        if not isinstance(user_or_id, TelegramUser):
            user = TelegramUser.objects.filter(telegram_id=user_or_id).first()
        else:
            user = user_or_id
            
        if(user):
            if with_dto:
                return TariffDto(user.tariff_plan)
            
            return user.tariff_plan
        else:
            return None

