from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message
import logging
import sqlite3


async def on_startup(dp):
    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    print('Bot launched')

if __name__:= '__main__':
    from aiogram import executor
    from handlers import dp
    executor.start_polling(dp, on_startup=on_startup)