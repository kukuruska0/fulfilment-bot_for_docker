from aiogram.utils.formatting import *

from app.services.translater import t as transl

from aiogram.utils.i18n import gettext as _


# from app.apps.core.DTO import KeywordsDto, TariffDto
# from app.apps.core.models import Search


class Messager:

    @staticmethod
    def empty():
        return Text('')

    @staticmethod
    def start():
        return as_list(
            Bold(_('Выберите язык')),
        )

    # @staticmethod
    # def start():
    #     return as_list(
    #         Bold(_('Здравствуйте!\n\nВыберите нужный пункт')),
    #     )

    @staticmethod
    def calculation():
        return as_list(
            Bold(_('https://t.me/Batiscafa')),
        )

    @staticmethod
    def product():
        return as_list(
            Bold(_("""Привет, я Вера, рада видеть тебя на нашем фулфилменте\nГрафик заборов с ТЯК: понедельник, среда и пятница.\n\nСтоимость:\n1 тюк - 1000 р.\nОт 5 тюков - 700 р./тюк\nОт 10 тюков - 600 р./тюк\n\nСадовод, Южные ворота и КАРГО\nот 1200р р./тюк\n\nКонтакты для забора:\n https://t.me/vera_fulfillment""")),
        )

    @staticmethod
    def price():
        return as_list(
            Bold(_('https://docs.google.com/spreadsheets/d/1PFVLzmoJlY48RNd2O17q9x81GvPmGQuz47XsyhI6Dpg/edit#gid=0')),
        )

    @staticmethod
    def shipment():
        return as_list(
            Bold(_('Выберите нужный пункт:')),
        )

    @staticmethod
    def address():
        return as_list(
            Bold(_("""Наш адрес:\nУлица 65 лет Победы, 1лит2Д\nЛюберцы, Московская область\n\nhttps://yandex.ru/navi/?whatshere%5Bzoom%5D=18&whatshere%5Bpoint%5D=37.884100%2C55.685127&lang=ru&from=navi""")),
        )

    @staticmethod
    def spoilage():
        return as_list(
            Bold(_('По поводу брака пишите своему менеджеру, который координировал вашу отгрузку.')),
        )

    @staticmethod
    def complaint():
        return as_list(
            Bold(_('Контакты по рекламациям:\n\nhttps://t.me/Elena_Bugrimova')),
        )

    @staticmethod
    def links():
        return as_list(
            Bold(_('Ссылки на наши соц.сети и сайты')),
        )
