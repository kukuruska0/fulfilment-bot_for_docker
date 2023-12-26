from aiogram.fsm.state import State, StatesGroup


class GetUsername(StatesGroup):
    get_username = State()
