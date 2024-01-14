import logging

from aiogram import Bot, Dispatcher

from app.apps.core.bot.routes.user_router import router as core_router
# from app.apps.core.bot.routes.admin_router import router as admin_router
from app.config.bot import MIDDLEWARE, RUNNING_MODE, RunningMode, TG_TOKEN

bot = Bot(TG_TOKEN, parse_mode="HTML")

dispatcher = Dispatcher()
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def _register_routers() -> None:
    dispatcher.include_router(core_router)
    # dispatcher.include_router(admin_router)


# async def _set_bot_commands() -> None:
#     await bot.set_my_commands(
#         [
#             BotCommand(command="/tariff", description=t('buttons.bot.tariff')),
#             BotCommand(command="/start", description=t('buttons.bot.start')),
#             BotCommand(command="/reload", description=t('buttons.bot.status')),
#         ]
#     )

# def _register_middleware() -> None:
#     for m in MIDDLEWARE:
#         dispatcher.update.outer_middleware.register(m())


@dispatcher.startup()
async def on_startup() -> None:
    # Register all routers
    _register_routers()
    # _register_middleware()

    # Set default commands
    # await _set_bot_commands()


def run_polling() -> None:
    dispatcher.run_polling(bot,
                           #    allowed_updates=dispatcher.resolve_used_update_types()
                           )


def run_webhook() -> None:
    raise NotImplementedError("Webhook mode is not implemented yet")


if __name__ == "__main__":
    if RUNNING_MODE == RunningMode.LONG_POLLING:
        run_polling()
    elif RUNNING_MODE == RunningMode.WEBHOOK:
        run_webhook()
    else:
        raise RuntimeError(f"Unknown running mode: {RUNNING_MODE}")
