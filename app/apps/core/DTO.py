from typing import List
from django.db.models import Model
import json
from app.apps.core.models import Search, TariffPlan, TelegramUser
from app.apps.core.bot.enum import SearchType
from app.services.has_attributes import HasAttributes


class DTO(HasAttributes):
    def __init__(self, data: dict | Model|None):
        if isinstance(data, Model):
            data = data.__dict__

        if(data):
            self.set_attributes(data)

    def to_json(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        dict = self.__dict__
        
        for key, item in dict.items():
            if isinstance(item, DTO):
                dict[key] = item.to_dict()
                
            elif isinstance(item, Model):
                dict[key] = item.__dict__
                
        return dict

    


class TariffDto(DTO):
    id: int | str = None
    name = None
    group_quantity = 0
    keyword_quantity = 0
    daemon_hours_quantity = 0
    allowed_searches = 0
    is_expired = 0
