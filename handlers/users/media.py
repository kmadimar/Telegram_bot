from aiogram.types import ContentType, Message
from loader import dp

@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(message: Message):
    await message.reply(message.photo[-1].file_id)

@dp.message_handler(text='/photo')
async def send_photo(message: Message):
    chat_id=message.from_user.id
    photo_file_id='AgACAgIAAxkBAAIBfWLuUk-0G40xh8nPxKkcVQJLQ_a7AAKLvjEbLORxS4svXCvju4-fAQADAgADeAADKQQ'
    await dp.bot.send_photo(chat_id=chat_id,photo=photo_file_id)