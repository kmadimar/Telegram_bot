from aiogram import types
from aiogram.types import CallbackQuery, Message, InputFile

from keyboards.inline import ikb_menu_dostup, ikb_menu_video, ikb_menu_questions, ikb_menu_start
from loader import dp



@dp.message_handler(text='❓ Ответы на частые вопросы')
async def show_inline(message: types.Message):
    replys = InputFile(path_or_bytesio='media/replys.jpg')
    await message.answer_photo(photo=replys)
    await message.answer('На большинство вопросов мы уже подготовили ответы, чтобы сэкономить Ваше и наше время 😉️\n'
                         f'        \n'
                         f'Листайте стрелочки вправо и влево, выбирайте нужный Вам вопрос.', reply_markup=ikb_menu_questions)


@dp.callback_query_handler(text='Презентация')
async def send_message(call: CallbackQuery):
    await call.message.answer(f'Для того, чтобы Вам было удобно, рассказывать буду в двух форматах - голосом и текстом.\n'
                              f'                                                                   \n'
                              f'😉️ Вы можете или послушать, или почитать, или и то и другое!'
                              f'                                                                   \n'
                              f'📌️ Хорошо?'
                              f'                                                                   \n'
                              f' Тогда переходим к сути 🙂️\n',reply_markup=ikb_menu_start)

@dp.callback_query_handler(text='Презентация2')
async def send_message(call: CallbackQuery):
    photo_bytes = InputFile(path_or_bytesio='media/planrosta.jpg')
    audio1=InputFile(path_or_bytesio='media/суть1.ogg')
    audio2 =InputFile(path_or_bytesio='media/суть2.ogg')
    await call.message.answer_audio(audio=audio1)
    await call.message.answer_audio(audio=audio2)
    await call.message.answer_photo(photo=photo_bytes)
    await call.message.answer(f'«План Роста»-  это 2 в 1 .Как шампунь с кондиционером)))\n'
                              f'                                                                   \n'
                              f'☝🏻️ Во-первых - это образовательный проект. Испытываем на себе и рассказываем Вам (наглядно и пошагово) как продвигать свои продукты, товары или услуги в Телеграм.\n'
                              f'                                                                   \n'
                              f'✌🏻️ Во-вторых - это проект, который дает уникальную возможность зарабатывать на его же перепродаже.\n')
    await call.message.answer(f'🤔️ Почему уникальную? Ну посудите сами:'
                              f'                                                                   \n'
                              f'🟣 У нас есть партнерская программа. 4 - х уровневая'
                              f'                                                                   \n'
                              f'🟣 С первого уровня(то есть с личной продажи) Вы зарабатываете сразу же на свою карту или электронный кошелек 1000 рублей.'
                              f'                                                                   \n'
                              f'🟣 Когда Ваш партнер продаст доступ(это второй уровень), Вы заработаете на полном пассиве - 150 рублей.С третьего и четвертого уровней по 100 и 50 рублей соответственно.'
                              f'🟣 Выплаты партнерских вознаграждений - ежедневно от 150 рублей.'
                              f'🔥️ ЭТО ПОЛНЫЙ ПАССИВ!')
    await call.message.answer(f'🟣 Для продвижения нашего проекта мы создали бота, вот этого, с которым Вы сейчас общаетесь.\n'
                              f'И Вам дадим шаблон, чтобы ничего не придумывать и работать по готовой системе.\n'
                              f'                                                                   \n'
                              f'🟣 Этот бот будет работать с Вашими клиентами и отвечать на самые частые вопросы. Даже когда Вы отдыхаете или занимаетесь личными делами.\n'
                              f'                                                                   \n'
                              f'🟣 Но где взять клиентов, с которыми будет работать бот?  Об этом - подробнейшее авторское обучение на нашем сайте.')
    await call.message.answer('Для навигации в боте отправьте сообщение с текстом /menu или выберите Меню в левом углу из списка комманд')



@dp.callback_query_handler(text='Ответ1')
async def send_message(call: CallbackQuery):
    audio_reply1= InputFile(path_or_bytesio='media/вложения.ogg')
    await call.message.answer_audio(audio=audio_reply1)
    await call.message.answer('Да, скрывать не будем. Вложения действительно нужны. В интернете в принципе без вложений не заработать.\n'
                              f'                 \n'
                              f'Любой товар, услугу или проект нужно продвигать. А это либо платная реклама, либо рассылки. Для рассылок и инвайтинга нужны расходники.\n'
                              f'Никто Вас не заставляет и не принуждает, определяете сами сколько Вам комфортно вкладывать в свое развитие.\n'
                              f'                 \n'
                              f'И бот, с которым Вы сейчас общаетесь тоже платный. Сам шаблон мы дадим бесплатно. А вот платформа, на которой он работает, стоит 750 рублей в месяц. Но зато бот работает круглосуточно и освобождает десятки часов Вашего личного времени.\n'
                              f'                 \n'
                              f'Первые две недели им можно пользоваться бесплатно. За две недели Вам нужно сделать 3 продажи, чтобы:\n'
                              f'                 \n'
                              f'🟣 отбить стоимость проекта'
                              f'                 \n'
                              f'🟣 заработать на следующий месяц работы бота\n'
                              f'                 \n'
                              'f🟣 отбить вложения в расходники\n'
                              'f       \n'
                              'f🟣 и выйти в плюс!\n'
                              f'Как думаете, с такими инструментами это возможно?'
                              'f       \n'
                              f'😉️ Да, конечно!')

@dp.callback_query_handler(text='Ответ2')
async def send_message(call: CallbackQuery):
    audio_reply2 = InputFile(path_or_bytesio='media/2 не получится.ogg')
    await call.message.answer_audio(audio=audio_reply2)
    await call.message.answer('Если Вы совсем ничего делать не будете, то - да. Может.\n'
                              f'                                                     \n'
                              f'А если серьезно - мы все для Вас подготовили, берите и делайте. Просто повторяйте.')

@dp.callback_query_handler(text='Ответ3')
async def send_message(call: CallbackQuery):
    await call.message.answer('У нас в проекте люди с разным уровнем подготовки. Кто-то быстро адаптируется, кому-то требуется время.\n'
                              f'                                                     \n'
                              f'Мы стараемся помогать всем в чате поддержки\n'
                              f'                                                     \n'
                              f'Но и от Вас, конечно же, требуется внимательность и желание научится новому. Мы поможем!')

@dp.callback_query_handler(text='Ответ4')
async def send_message(call: CallbackQuery):
    audio_reply4 = InputFile(path_or_bytesio='media/Почему нужно платить.ogg')
    await call.message.answer_audio(audio=audio_reply4)
    await call.message.answer('Мы даем качественную информацию. Даем готовые инструменты для работы. Помогаем свои партнерам. \n'
                              f'                                                     \n'
                              f'Это должно оплачиваться и это нормально. Правда ведь?')

@dp.callback_query_handler(text='Ответ5')
async def send_message(call: CallbackQuery):
    await call.message.answer('Ну, конечно, нет))) Бросать вас никто не собирается. \n'
                              f'Доступы выдаем вручную. Задержки могут быть из-за разных часовых поясов или просто из-за занятости. \n'
                              f'                                                     \n'
                              f'В процессе обучения будут возникать вопросы - их задавайте мне или в наш общий чат поддержки.')

@dp.callback_query_handler(text='Ответ6')
async def send_message(call: CallbackQuery):
    audio_reply6 = InputFile(path_or_bytesio='media/Могу я заплатить после обучения.ogg')
    await call.message.answer_audio(audio=audio_reply6)
    await call.message.answer('Такой возможности у нас не предусмотрено. \n'
                              f'                                                     \n'
                              f'И пользы Вам бесплатный доступ не принесет.')

@dp.callback_query_handler(text='Ответ7')
async def send_message(call: CallbackQuery):
    audio_reply7 = InputFile(path_or_bytesio='media/У меня нет денег.ogg')
    await call.message.answer_audio(audio=audio_reply7)
    await call.message.answer('Их практически никогда не бывает в нужном количестве. А если ничего не менять в своей жизни, то их точно не прибавится. '
                              f'                                                     \n'
                              f'У нас Вы получите знания и возможность быстро зарабатывать. Нужно Вам это сейчас или нет - решаете сами.')

@dp.callback_query_handler(text='Ответ8')
async def send_message(call: CallbackQuery):
    audio_reply8 = InputFile(path_or_bytesio='media/время.ogg')
    await call.message.answer_audio(audio=audio_reply8)
    await call.message.answer(f'У всех разные темпы и уровень подготовки. \n'
                              f'\n'
                              f'Сказать точно, сколько времени будет уходить у Вас я не смогу. Но рассчитывайте примерно на 2-3 часа в день.')

@dp.callback_query_handler(text='Ответ9')
async def send_message(call: CallbackQuery):
    audio_reply9 = InputFile(path_or_bytesio='media/гарантии заработка.ogg')
    await call.message.answer_audio(audio=audio_reply9)
    await call.message.answer('Мы не можем дать гарантий, что Вы 100% будете зарабатывать. Это зависит только от Вас и ваших действий.\n'
                              f'\n'
                              f'Но то, что система работает - подтверждают чеки и отзывы нашей команды!')

@dp.callback_query_handler(text='Ответ10')
async def send_message(call: CallbackQuery):
    audio_reply10 = InputFile(path_or_bytesio='media/компания.ogg')
    await call.message.answer_audio(audio=audio_reply10)
    await call.message.answer('Проект "План Роста" - это объединение людей, заинтересованных в быстром и автоматизированном заработке. А все по отдельности - мы фрилансеры. И работаем сами на себя.')

@dp.callback_query_handler(text='Ответ11')
async def send_message(call: CallbackQuery):
    audio_reply11 = InputFile(path_or_bytesio='media/с телефона.ogg')
    await call.message.answer_audio(audio=audio_reply11)
    await call.message.answer('У нас обучение создано как раз на основе работы с телефона Андроид. Для Айфонов будет гораздо сложнее, но варианты тоже есть. \n'
                              f'\n'
                              f'Настройку бота - лучше сделать с компьютера, а потом можно и с телефона им пользоваться.')

@dp.callback_query_handler(text='Ответ12')
async def send_message(call: CallbackQuery):
    audio_reply12 = InputFile(path_or_bytesio='media/с телефона.ogg')
    await call.message.answer_audio(audio=audio_reply12)
    await call.message.answer('Да, без бота тоже можно работать. Возьмете свою партнерскую ссылку и будете общаться с каждым клиентом самостоятельно.')

@dp.callback_query_handler(text='Ответ13')
async def send_message(call: CallbackQuery):
    await call.message.answer(f'Мы не пирамида.\n'
                              f'У нас в основе не идея и выдуманные ценности, а реальной курс по продвижению. Шаблон бота для общения с клиентами. \n'
                              f'\n'
                              f'Это цифровые товары. Вы можете ими пользоваться и перепродавать.')

@dp.callback_query_handler(text='Ответ14')
async def send_message(call: CallbackQuery):
    audio_reply14 = InputFile(path_or_bytesio='media/лохотрон, развод.ogg')
    await call.message.answer_audio(audio=audio_reply14)
    await call.message.answer('Мы все говорим честно заранее. И не обещаем, что Вы купите у нас доступ и завтра на Вас посыпятся деньги.\n'
                              f'\n'
                              f'Нужно будет работать. А инструкции, инструменты  и моральная поддержка - с нас)))')


@dp.callback_query_handler(text='Ответ15')
async def send_message(call: CallbackQuery):
    audio_reply15 = InputFile(path_or_bytesio='media/другая страна.ogg')
    await call.message.answer_audio(audio=audio_reply15)
    await call.message.answer(f'Да, можете. \n'
                              f'\n'
                              f'Самое главное даже не купить доступ в наш проект. Самое главное - проверить, а сможете ли Вы получать переводы из других стран, в том числе и из России.\n'
                              f'\n'
                              f'Смотрите все возможные варианты - электронные кошельки (Киви, Юмани, Пайер), системы денежных переводов, биржи обмена валют')

@dp.callback_query_handler(text='Ответ16')
async def send_message(call: CallbackQuery):
    audio_reply16 = InputFile(path_or_bytesio='media/с айфона.ogg')
    await call.message.answer_audio(audio=audio_reply16)
    await call.message.answer(f'Да, удобного приложения для работы в Телеграм для айфонов нет.\n'
                              f'\n'
                              f'Но есть несколько вариантов:\n'
                              f'\n'
                              f'- ручные рассылки в личные сообщения;\n'
                              f'\n'
                              f'- использование софта;\n'
                              f'\n'
                              f'- платная реклама.')

@dp.callback_query_handler(text='Ответ17')
async def send_message(call: CallbackQuery):
    audio_reply17 = InputFile(path_or_bytesio='media/юридическое оформление.ogg')
    await call.message.answer_audio(audio=audio_reply17)
    await call.message.answer('Пока Вы только начинаете, можно ничего не оформлять. \n'
                              f'\n'
                              f'Когда выйдете на стабильный доход - оформляете самозанятость и платите 4% налогов. Это очень просто делается. Даже ездить никуда не придется.')


@dp.callback_query_handler(text='Ответ18')
async def send_message(call: CallbackQuery):
    audio_reply18 = InputFile(path_or_bytesio='media/подумаю.ogg')
    await call.message.answer_audio(audio=audio_reply18)
    await call.message.answer('Конечно, подумайте! Это важное решение.\n'
                              f'Просто соотнесите стоимость входа в проект и ту ценность, которую Вы получите))')
