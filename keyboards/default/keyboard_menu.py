from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='😍 Чеки и отзывы'),
            KeyboardButton(text='🔑 Гостевой доступ'),
        ],
        [
            KeyboardButton(text='📹 Видео о проекте',),
        ],
        [
            KeyboardButton(text='❓ Ответы на частые вопросы'),
        ],
        [
            KeyboardButton(text='🤔 Стоимость'),
            KeyboardButton(text='💳 Оплата'),
        ],
        [
            KeyboardButton(text='✉️ Связаться со мной', url='https://t.me/kammm96')
        ]
    ],
    resize_keyboard=True
)
