from aiogram import types
from aiogram.types import InputFile

from loader import dp
from keyboards.inline import ikb_menu_dostup, ikb_menu_video,ikb_menu_payment, ikb_menu_contact,ikb_menu_otzyv,ikb_menu_questions


@dp.message_handler(text='😍 Чеки и отзывы')
async def buttons_test(message: types.Message):
    await message.answer(f'Вы можете почитать отзывы о проекте и посмотреть чеки от продаж в нашей группе '
                         ,reply_markup=ikb_menu_otzyv)

@dp.message_handler(text='🔑 Гостевой доступ')
async def show_inline(message: types.Message):
    await message.answer(f'Наше обучение находится на собственном сайте.\n'
                         f'                                              \n'
                         f'Попасть в него можно только по ключу активации. \n'
                         f'Его Вы обязательно получите после оплаты доступа в наш проект.\n'
                         f'                                              \n'
                         f'Но сейчас Вы можете зайти и посмотреть, как там все устроено. \n'
                         f'Ознакомиться с курсом, его структурой и несколькими открытыми уроками.\n'
                         f'                                              \n'
                         f'📍️ Важно! Регистрироваться не нужно!\n'
                         f'                                              \n'
                             f'Переходите по ссылочке 👇🏼️\n'
                         , reply_markup=ikb_menu_dostup)

@dp.message_handler(text='📹 Видео о проекте')
async def buttons_video(message: types.Message):
    await message.answer(f'{message.from_user.first_name}, мы подготовили для Вас короткое видео о проекте.\n'
                         f'                                              \n'
                         f'Посмотрите, не пожалейте 5 минут времени, зато будет понятно для чего нужен этот проект и как тут зарабатывать 🙂️\n'
                         ,reply_markup=ikb_menu_video)



@ dp.message_handler(text='🤔 Стоимость')
async def buttons_fee(message: types.Message):
    fee=InputFile(path_or_bytesio='media/fee.jpg')
    fee2=InputFile(path_or_bytesio='media/fee2.jpg')
    await message.answer_photo(photo=fee)
    await message.answer(f'Доступ в проект стоит 1490 рублей.\n'
                         f'                                              \n'
                         f'Специально сделали такую невысокую цену (подобные курсы стоят от 5000 рублей и выше),'
                         f'понимаем какая сейчас вокруг ситуация и просто хотим помочь людям получить новые знания,'
                         f'опыт и возможность зарабатывать практически на автомате.')
    await message.answer_photo(photo=fee2)
    await message.answer(f'🔥️ За 1490 рублей Вы получаете готовую систему заработка в Телеграм.\n'
                         f'                                              \n'
                         f'🟣 Подробный пошаговый курс по продвижению в Телеграм.\n'
                         f'В нем разбираем быстрые ручные методы продвижения - инвайтинг, рассылки в личные сообщения пользователям Телеграм, рассылки по пиар-чатам.\n'
                         f'                                              \n'
                         f'🟣 Автоматизация инвайтинга - уроки по работе с программой для раскрутки Ваших рекламных групп и сама программа!\n'
                         f'                                              \n'
                         f'🟣 Уроки по тотальной автоматизации Телеграм\n'
                         f'                                              \n'
                         f'🟣 Для партнеров, которые будут продвигать наш проект "План Роста" - шаблон бота, который будет круглосуточно обрабатывать входящие заявки, общаться с Вашими потенциальными клиентами и отправлять Ваши реквизиты для оплаты.')
    await message.answer('Кроме того:\n'
                         f'                                              \n'
                         f'📌️ Будете зарабатывать сразу же 1000 рублей на руки от перепродажи нашего курса\n'
                         f'                                              \n'
                         f'📌️ Примете участие в партнерской программе и сможете зарабатывать на полном пассиве (выплаты ежедневные от 150 рублей)\n'
                         f'                                              \n'
                         f'📌️ Получите доступ в чат поддержки\n'
                         f'                                              \n'
                         f'📌️ Сможете принимать участие в розыгрышах внутри проекта')
@ dp.message_handler(text='💳 Оплата')
async def buttons_payment(message: types.Message):

    await message.answer(f'🔥️ Прекрасно! Будем рады видеть Вас в нашем проекте!\n'
                         f'                                              \n'
                         f'{message.from_user.first_name}!, вы можете оплатить по ссылке ниже.\n'
                         f'                                              \n'
                         f'📌️ После оплаты, обязательно отправьте чек по кнопке ниже "Связаться cо мной", на котором видно дату, время и получателя платежа.\n' 
                        f'                                              \n'
                         f'🔓️ Я проверю поступила ли оплата и выдам Вам все необходимые доступы.\n'
                         f'                                              \n'
                         f'Если у вас не получилось оплатить, или вы хотите оплатить другим методом напишите мне.\n'
                         ,reply_markup=ikb_menu_payment)

@ dp.message_handler(text='✉️ Связаться со мной')
async def buttons_contact(message):
    await message.answer('Перейдите по ссылке ниже чтобы связаться мо мной',reply_markup=ikb_menu_contact)

