import logging

from aiogram import types

from .bot import dp
from .dialogs import msg
from . import use_case


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    logger = logging.getLogger("Start Handler")
    logger.info(f'From user: {message.from_user.first_name}. Text: {message.text}')
    user_name = message.from_user.first_name
    await message.answer(msg.start_message.format(name=user_name))


@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    logger = logging.getLogger("Help Handler")
    logger.info(f'From user: {message.from_user.first_name}. Text: {message.text}')
    await message.answer(msg.help_message)


@dp.message_handler(commands=['search'])
async def search(message: types.Message):
    logger = logging.getLogger("Search Handler")
    logger.info(f'From user: {message.from_user.first_name}. Text: {message.text}')
    s = message.text.split('/search ')
    if len(s) != 2:
        await message.answer(msg.search_help)
    else:
        await message.answer(use_case.get_search(s[1]))


@dp.message_handler()
async def unknown_message(message: types.Message):
    logger = logging.getLogger("Unknown Message")
    logger.info(f'From user: {message.from_user.first_name}. Text: {message.text}')
    await message.answer(msg.unknown_message)
