from aiogram import types
from loader import dp

@dp.message_handler(text='/help')

async def command_start(message: types.Message):
    await message.answer(f'Hi {message.from_user.full_name}!\n'
                         f'Do you need help? :{message.from_user.id}')