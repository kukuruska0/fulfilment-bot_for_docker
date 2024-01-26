from pathlib import Path

from aiogram.utils.i18n import I18n, SimpleI18nMiddleware, FSMI18nMiddleware

WORKDIR = Path(__file__).parent.parent.parent
i18n = I18n(path=WORKDIR/'locales', default_locale='ru', domain='fulfilmentbot')
i18n_middleware = FSMI18nMiddleware(i18n=i18n)
