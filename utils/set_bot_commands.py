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
from data.config import admins

user_commands = [
    BotCommand('start', 'Запустить бота'),
    BotCommand('menu', 'Меню')
]


# Команды для админов
admin_commands = [
    BotCommand('start', 'Запустить бота'),
    BotCommand("faq", "ℹ FAQ"),
    BotCommand("db", "📦 Получить Базу Данных"),
    BotCommand("log", "🖨 Получить логи"),
]


# Установка команд
async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(user_commands, scope=BotCommandScopeDefault())

    for admin in admins:
        try:
            await dp.bot.set_my_commands(admin_commands, scope=BotCommandScopeChat(chat_id=admin))
        except:
            pass

# Установка команд
#async def set_default_commands(dp: Dispatcher):
 #   await dp.bot.set_my_commands(user_commands, scope=BotCommandScopeDefault())
