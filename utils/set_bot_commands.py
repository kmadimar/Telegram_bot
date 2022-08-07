#from aiogram import types

#async def set_default_commands(dp):
    #await dp.bot.set_my_commands([
        #types.BotCommand('start', 'Запустить бота'),
        #types.BotCommand('menu', 'Меню'),
        #types.BotCommand('help', 'Помощь')
    #])


# - *- coding: utf- 8 - *-
from aiogram import Dispatcher
from aiogram.types import BotCommand, BotCommandScopeDefault

#from tgbot.data.config import get_admins

# Команды для юзеров
user_commands = [
    BotCommand('start', 'Запустить бота'),
    BotCommand('menu', 'Меню')
]

# Установка команд
async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(user_commands, scope=BotCommandScopeDefault())
