from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu_ok = InlineKeyboardMarkup(row_width=2,
                             inline_keyboard=[
                                  [
                                      InlineKeyboardButton(text='✅Да, конечно',callback_data='Презентация')
                                  ],
                              ])
ikb_menu_start = InlineKeyboardMarkup(row_width=2,
                             inline_keyboard=[
                                  [
                                      InlineKeyboardButton(text='📌️ Хорошо',callback_data='Презентация2')
                                  ],
                              ])

ikb_menu_otzyv = InlineKeyboardMarkup(row_width=2,
                             inline_keyboard=[
                                  [
                                      InlineKeyboardButton(text= '😍 Чеки и отзывы',url='https://t.me/plan_rosta22')
                                  ],
                              ])

ikb_menu_dostup = InlineKeyboardMarkup(row_width=2,
                             inline_keyboard=[
                                  [
                                      InlineKeyboardButton(text= '🔑 Гостевой доступ',url='https://tg2022.ru/course/')
                                  ],
                              ])
ikb_menu_video = InlineKeyboardMarkup(row_width=2,
                             inline_keyboard=[
                                  [
                                      InlineKeyboardButton(text= '📹 Видео о проекте',url='https://www.youtube.com/watch?v=d4-QzzrNyu0')
                                  ],
                              ])

ikb_menu_payment = InlineKeyboardMarkup(row_width=2,
                             inline_keyboard=[
                                  [
                                      InlineKeyboardButton(text= 'Перейти к оплате',url='https://oplata.qiwi.com/form?invoiceUid=7cf244ce-cc68-4c38-a04e-a844cd0acd8e')
                                  ],
                                 [
                                      InlineKeyboardButton(text= 'Связаться cо мной',url='https://t.me/kammm96')
                                  ],
                              ])

ikb_menu_contact = InlineKeyboardMarkup(row_width=2,
                             inline_keyboard=[
                                 [
                                      InlineKeyboardButton(text= '✉️ Связаться со мной',url='https://t.me/kammm96')
                                  ],
                              ])

ikb_menu_questions = InlineKeyboardMarkup(row_width=2,
                             inline_keyboard=[
                                 [
                                    InlineKeyboardButton(text= 'Нужны ли вложения ❓',callback_data='Ответ1')
                                ],
                                 [
                                    InlineKeyboardButton(text= 'Может получиться так что я не заработаю ❓',callback_data='Ответ2')
                                 ],
                                 [
                                    InlineKeyboardButton(text= 'У меня нет опыта, я справлюсь ❓',callback_data='Ответ3'),
                                  ],
                                 [
                                    InlineKeyboardButton(text= 'Почему нужно платить ❓',callback_data='Ответ4'),
                                  ],
                                 [
                                    InlineKeyboardButton(text= 'Вы меня не бросите после оплаты ❓',callback_data='Ответ5'),
                                  ],
                                 [
                                    InlineKeyboardButton(text= 'Могу я заплатить после обучения ❓',callback_data='Ответ6'),
                                  ],
                                 [
                                    InlineKeyboardButton(text= 'У меня нет денег ❓',callback_data='Ответ7'),
                                  ],
                                 [
                                    InlineKeyboardButton(text= 'Сколько времени занимает ❓',callback_data='Ответ8'),
                                  ],
                                 [
                                    InlineKeyboardButton(text= 'Какие вы даете гарантии ❓',callback_data='Ответ9'),
                                  ],
                                 [
                                    InlineKeyboardButton(text= 'Что за компания ❓',callback_data='Ответ10'),
                                  ],
                                 [
                                    InlineKeyboardButton(text= 'Можно работать с телефона ❓',callback_data='Ответ11'),
                                  ],

                                 [
                                     InlineKeyboardButton(text='Можно работать без бота ❓', callback_data='Ответ12'),

                                 ],
                                [
                                    InlineKeyboardButton(text= 'Это пирамида❓',callback_data='Ответ13'),

                                  ],
                                    [
                                    InlineKeyboardButton(text= 'Очередной лохотрон❓',callback_data='Ответ14'),

                                  ],
                                 [
                                    InlineKeyboardButton(text= 'Я не из России, смогу работатать ❓',callback_data='Ответ15'),
                                  ],
                                 [
                                    InlineKeyboardButton(text= 'У меня айфон, смогу работать ❓',callback_data='Ответ16'),
                                  ],
                                 [
                                    InlineKeyboardButton(text= 'Как юридический оформляется ❓',callback_data='Ответ17'),
                                  ],
                                 [
                                    InlineKeyboardButton(text= 'Мне надо подумать 🤔',callback_data='Ответ18'),
                                  ],


                              ])