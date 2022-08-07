from aiogram import types
from loader import dp
from keyboards.inline import ikb_menu_ok

@dp.message_handler(text='/start')

async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.first_name}!\n'
                         f'                                                                      \n'
                         f'Раз Вы это сейчас читаете, значит вас заинтересовало мое предложение😍\n'
                         f'                                                                      \n'
                         f'Я - Камила, партнёр проекта План Роста.\n'
                         f'                                                                      \n'
                         f'Для начала предлагаю вам ознакомиться с проектом с помощью бота.\n'
                         f'                                                                      \n'
                         f' Вы сможете узнать о проекте и найти ответы на самые часто задаваемые \n'
                         f'вопросы и понять подходит ли вам это предложение.\n'
                         f'                                                                      \n'
                         f'Если у вас останутся какие-то вопросы или вы захотите поговорить лично - напишите мне\n'
                         f'                                                                      \n'
                         f'ДОГОВОРИЛИСЬ ?',reply_markup=ikb_menu_ok)




