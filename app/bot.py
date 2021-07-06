from aiogram import Bot
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher

from app.config import config

# Creating bot
bot = Bot(token=config.bot_token)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())
