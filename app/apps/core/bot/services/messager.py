from aiogram.types import *
from app.services.translater import t as transl
from aiogram.utils.formatting import *
from app.apps.core.DTO import KeywordsDto, TariffDto
from app.apps.core.models import Search


class Messager:

    @staticmethod
    def empty():
        return Text('')

        
    @staticmethod
    def action_exception(msg):
        return as_list(
            Bold("❌"+ transl('wrong.action')),
            msg,
        )



    @staticmethod
    def q_reached():
        return Bold(transl('info.max_count_reached'))

    @staticmethod
    def choise_action():
        return as_list(
            Bold(transl('buttons.choice_action'))
        )
        
    

    @staticmethod
    def about():
        return as_list(
            Bold(transl('get_started')),
        )
        
    

    @staticmethod
    def hello():
        return as_list(
            Bold(transl('say_hello')),
        )


