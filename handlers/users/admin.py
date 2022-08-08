# - *- coding: utf- 8 - *-
import asyncio

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.utils.exceptions import CantParseEntities


from loader import dp, bot

from utils.filter import IsAdmin

# Рассылка
@dp.message_handler(IsAdmin(), text="📢 Рассылка", state="*")
async def functions_ad(message: Message, state: FSMContext):
    await state.finish()

    await state.set_state("here_ad_text")
    await message.answer("<b>📢 Введите текст для рассылки пользователям</b>\n"
                         "❕ Вы можете использовать HTML разметку")

########################################### CALLBACKS ###########################################
# Подтверждение отправки рассылки
@dp.callback_query_handler(IsAdmin(), text_startswith="confirm_ad", state="here_ad_confirm")
async def functions_ad_confirm(call: CallbackQuery, state: FSMContext):
    get_action = call.data.split(":")[1]

    send_message = (await state.get_data())['here_ad_text']
    get_users = get_all_usersx()
    await state.finish()

    if get_action == "yes":
        await call.message.edit_text(f"<b>📢 Рассылка началась... (0/{len(get_users)})</b>")
        asyncio.create_task(functions_ad_make(send_message, call))
    else:
        await call.message.edit_text("<b>📢 Вы отменили отправку рассылки ✅</b>")


# Отправка рассылки
async def functions_ad_make(message, call: CallbackQuery):
    receive_users, block_users, how_users = 0, 0, 0
    get_users = get_all_usersx()

    for user in get_users:
        try:
            await bot.send_message(user['user_id'], message, disable_web_page_preview=True)
            receive_users += 1
        except:
            block_users += 1

        how_users += 1

        if how_users % 10 == 0:
            await call.message.edit_text(f"<b>📢 Рассылка началась... ({how_users}/{len(get_users)})</b>")

        await asyncio.sleep(0.05)

    await call.message.edit_text(
        f"<b>📢 Рассылка была завершена ✅</b>\n"
        f"👤 Пользователей получило сообщение: <code>{receive_users} ✅</code>\n"
        f"👤 Пользователей не получило сообщение: <code>{block_users} ❌</code>"
    )





#### ПРИНЯТИЕ ДАННЫХ ########################################
# Принятие текста для рассылки
@dp.message_handler(IsAdmin(), state="here_ad_text")
async def functions_ad_get(message: Message, state: FSMContext):
    await state.update_data(here_ad_text="📢 Рассылка.\n" + str(message.text))
    get_users = get_all_usersx()

    try:
        cache_msg = await message.answer(message.text)
        await cache_msg.delete()

        await state.set_state("here_ad_confirm")
        await message.answer(
            f"<b>📢 Отправить <code>{len(get_users)}</code> юзерам сообщение?</b>\n"
            f"{message.text}",
            reply_markup=ad_confirm_inl,
            disable_web_page_preview=True
        )
    except CantParseEntities:
        await message.answer("<b>❌ Ошибка синтаксиса HTML.</b>\n"
                             "📢 Введите текст для рассылки пользователям.\n"
                             "❕ Вы можете использовать HTML разметку.")





# Принятие суммы для изменения баланса пользователя
@dp.message_handler(IsAdmin(), state="here_profile_set")
async def functions_profile_balance_set_get(message: Message, state: FSMContext):
    if message.text.isdigit():
        if 0 <= int(message.text) <= 1000000000:
            user_id = (await state.get_data())['here_profile']
            await state.finish()

            get_user = get_userx(user_id=user_id)
            update_userx(user_id, user_balance=message.text)

            await message.answer(
                f"<b>✅ Пользователю <a href='tg://user?id={get_user['user_id']}'>{get_user['user_name']}</a> "
                f"изменён баланс на <code>{message.text}₽</code></b>")

            await message.answer(open_profile_search(user_id), reply_markup=profile_search_finl(user_id))
        else:
            await message.answer("<b>❌ Сумма изменения не может быть меньше 0 и больше 1 000 000 000</b>\n"
                                 "💰 Введите сумму для изменения баланса")
    else:
        await message.answer("<b>❌ Данные были введены неверно.</b>\n"
                             "💰 Введите сумму для изменения баланса")


# Отправка сообщения пользователю
@dp.callback_query_handler(IsAdmin(), text_startswith="admin_user_message", state="*")
async def functions_profile_user_message(call: CallbackQuery, state: FSMContext):
    await state.update_data(here_profile=call.data.split(":")[1])

    await state.set_state("here_profile_message")
    await call.message.edit_text("<b>💌 Введите сообщение для отправки</b>\n"
                                 "⚠ Сообщение будет сразу отправлено пользователю.")


# Принятие сообщения для пользователя
@dp.message_handler(IsAdmin(), state="here_profile_message")
async def functions_profile_user_message_get(message: Message, state: FSMContext):
    user_id = (await state.get_data())['here_profile']
    await state.finish()

    get_message = "<b>💌 Вам сообщение:</b>\n" + clear_html(message.text)
    get_user = get_userx(user_id=user_id)

    await message.bot.send_message(user_id, get_message)
    await message.answer(f"<b>✅ Пользователю <a href='tg://user?id={get_user['user_id']}'>{get_user['user_name']}</a> "
                         f"было отправлено сообщение:</b>\n"
                         f"{get_message}")

    await message.answer(open_profile_search(user_id), reply_markup=profile_search_finl(user_id))


`
