from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

keyboard_button = [
    [KeyboardButton(text='🇺🇿 Uzbek'),
     KeyboardButton(text='🇷🇺 Russia'),
     ],
]

keyboard = ReplyKeyboardMarkup(keyboard=keyboard_button, resize_keyboard=True, row_width=1)

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True,
                                keyboard=[
                                    [KeyboardButton(text='Xizmat'),
                                     KeyboardButton(text='Maxsulot'),
                                     KeyboardButton(text='Orqaga'),
                                     ]], row_width=1
                                )

keyboard4 = ReplyKeyboardMarkup(resize_keyboard=True,
                                keyboard=[
                                    [KeyboardButton(text='Santexnik'),
                                     KeyboardButton(text='Elektrik'),
                                     KeyboardButton(text='Menu'),
                                     ]], row_width=1
                                )

keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True,
                                keyboard=[
                                    [KeyboardButton(text='Услуга'),
                                     KeyboardButton(text='Продукт'),
                                     KeyboardButton(text='Назад'),
                                     ]], row_width=1
                                )

keyboard3 = ReplyKeyboardMarkup(resize_keyboard=True,
                                keyboard=[
                                    [KeyboardButton(text='Сантехник'),
                                     KeyboardButton(text='Електрик'),
                                     KeyboardButton(text='Меню'),
                                     ]], row_width=1
                                )

keyboard7 = ReplyKeyboardMarkup(resize_keyboard=True,
                                keyboard=[
                                    [KeyboardButton(text='Tasdiqlash'),
                                     KeyboardButton(text='Ozgartirish'),
                                     ]], row_width=1
                                )

keyboard8 = ReplyKeyboardMarkup(resize_keyboard=True,
                                keyboard=[
                                    [KeyboardButton(text='Подтверждение'),
                                     KeyboardButton(text='Изменять'),
                                     ]], row_width=1
                                )

inline_keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='Перейти на сайт', url='https://www.darkor22.uz/uz')]])

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Saytga o'tish", url='https://www.darkor22.uz/uz')]])

# @dp.callback_query(lambda query: query.data.startswith('uz'))
# async def action_callback(callback_query: CallbackQuery):
#     await bot.send_message(callback_query.from_user.id, "Xizmatni tanlang", reply_markup=keyboard1)
#
#
# @dp.callback_query(lambda query: query.data.startswith('rus'))
# async def action_callback(callback_query: CallbackQuery):
#     await bot.send_message(callback_query.from_user.id, 'Выберите услугу', reply_markup=keyboard2)


# inline_keyboard1 = InlineKeyboardMarkup(
#                                        inline_keyboard=[
#                                            [InlineKeyboardButton(text='Xizmat', callback_data=f'xizmat'),
#                                             InlineKeyboardButton(text='Maxsulot', url='https://www.darkor22.uz/uz'),
#                                             ]]
#                                        )
#
#
#
# inline_keyboard2 = InlineKeyboardMarkup(
#                                        inline_keyboard=[
#                                            [InlineKeyboardButton(text='Услуга', callback_data=f'maxsulot'),
#                                             InlineKeyboardButton(text='Продукт', url='https://www.darkor22.uz/uz'),
#                                             ]]
#                                        )

key = ReplyKeyboardMarkup(resize_keyboard=True,
                          keyboard=[
                              [KeyboardButton(text='Manzilni yuborish', request_location=True),
                               ]], row_width=1
                          )

key1 = ReplyKeyboardMarkup(resize_keyboard=True,
                           keyboard=[
                               [KeyboardButton(text='Отправить местоположение', request_location=True),
                                ]], row_width=1
                           )

contact1 = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [KeyboardButton(text='Tugma orqali', request_contact=True),
                                    ]], row_width=1
                               )
