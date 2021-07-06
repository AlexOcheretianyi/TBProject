import logging
from aiogram import executor

from app.config import configure_logger
from app.handlers import dp


def main():
    configure_logger()
    logger = logging.getLogger('Main')
    logger.info('Bot Started')
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
