import asgiref.sync
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from app.apps.core.bot.enum import SearchStatus, SearchType
from asgiref.sync import sync_to_async, async_to_sync


class TariffPlan(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, unique=True)
    is_default = models.BooleanField(default=False)
    group_quantity = models.IntegerField()
    keyword_quantity = models.IntegerField()
    old_messages_offset = models.IntegerField()
    daemon_hours_quantity = models.IntegerField()
    allowed_searches = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name} - {self.group_quantity} групп'


    
class TelegramUser(models.Model):
    id=models.AutoField(primary_key=True)
    telegram_username = models.CharField(max_length=80)
    telegram_id = models.CharField(max_length=50, blank=True, null=True, unique=True)
    telegram_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    is_accepted_rules = models.BooleanField(default=False)
    tariff_plan = models.ForeignKey(
        TariffPlan, on_delete=models.SET_NULL, null=True, blank=True, related_name='telegram_user')
    expired_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_activity_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        tariff = 'none'
        if(self.tariff_plan):
            tariff = self.tariff_plan.name
            

        mess = '\n' 
        for_messages = {
            'telegram_id':self.telegram_id,
            'telegram_username':self.telegram_username,
            'telegram_name':self.telegram_name,
            'is_accepted_rules':self.is_accepted_rules,
            'tariff_plan': tariff,
            'last_activity_at':self.last_activity_at,
        }
        
        for key, value in for_messages.items():   
            mess  +=   f"{key}: {value}\n"
            
        return mess
