from aiogram.filters.callback_data import CallbackData


class UserCallbackData(CallbackData, prefix='user'):
    action: str
    type: str | None = None
    id: int | None = None
    name: str | None = None
    search_id: int | None = None
    tariff_id: int | None = None
    message_id: int | str | None = None
    keywords: dict | None = None
