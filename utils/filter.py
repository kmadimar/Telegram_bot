
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data.config import admins

# Проверка на админа
class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        if message.from_user.id in admins():
            return True
        else:
            return False