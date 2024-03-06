from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from keyboard_button import keyboard, keyboard1, keyboard4, inline_keyboard, contact1, keyboard7, keyboard8, key, \
    keyboard3, keyboard2, inline_keyboard1, key1

API_TOKEN = '6570822063:AAFxwU--5Whc66vdwuXaj1yBNVSosNsPIAw'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


class Form(StatesGroup):
    service_type = State()
    name_username = State()
    phone_number = State()
    comment = State()
    location = State()


import re


def validate_phone_number(phone_number):
    phone_regex_with_spaces = re.compile(r'^\+998 \d{2} \d{3} \d{2} \d{2}$')
    phone_regex_without_spaces = re.compile(r'^\+998\d{9}$')
    if phone_regex_with_spaces.match(phone_number) or phone_regex_without_spaces.match(phone_number):
        return True
    else:
        return False


@dp.message_handler(commands=['start'])
async def command_start_handler(message: types.Message):
    await message.answer("Tilni tanlang   /   Выберите язык", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in ['🇺🇿 Uzbek', 'Orqaga'])
async def rek_photo(message: types.Message):
    if message.text == '🇺🇿 Uzbek':
        await message.answer("Xizmatni tanlang", reply_markup=keyboard1)
    elif message.text == 'Orqaga':
        await message.answer("Tilni tanlang   /   Выберите язык", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in ['🇷🇺 Russia', 'Назад'])
async def rek_photo(message: types.Message):
    if message.text == '🇷🇺 Russia':
        await message.answer('Выберите услугу', reply_markup=keyboard2)
    elif message.text == 'Назад':
        await message.answer("Tilni tanlang   /   Выберите язык", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in ['Услуга', 'Продукт', 'Меню'])
async def rek_photo(message: types.Message):
    if message.text == 'Услуга':
        await message.answer('Услуга', reply_markup=keyboard3)
    elif message.text == 'Продукт':
        await message.answer('Перейти на сайт', reply_markup=inline_keyboard1)
    elif message.text == 'Меню':
        await message.answer('Выберите услугу', reply_markup=keyboard2)


@dp.message_handler(lambda message: message.text in ['Xizmat', 'Maxsulot', 'Menu'])
async def rek_photo(message: types.Message):
    if message.text == 'Xizmat':
        await message.answer("Xizmatni turini tanlang", reply_markup=keyboard4)
    elif message.text == 'Maxsulot':
        await message.answer("Saytga o'tish", reply_markup=inline_keyboard)
    elif message.text == 'Menu':
        await message.answer('Xizmatni tanlang', reply_markup=keyboard1)


@dp.message_handler(lambda message: message.text in ['Santexnik', 'Elektrik', 'Сантехник', 'Електрик'])
async def rek_photo(message: types.Message, state: FSMContext):
    if message.text == 'Santexnik':
        global xz_turi
        xz_turi = message.text
        async with state.proxy() as data:
            data['service_type'] = message.text
        await message.answer('Ism Familiya kirting:\nM-n :  "Soliyev Ikrom"')
        await Form.name_username.set()
    elif message.text == 'Elektrik':
        xz_turi = message.text
        async with state.proxy() as data:
            data['service_type'] = message.text
        await message.answer('Ism Familiya kirting:\nM-n :  "Soliyev Ikrom"')
        await Form.name_username.set()
    elif message.text == 'Сантехник':
        xz_turi = message.text
        async with state.proxy() as data:
            data['service_type'] = message.text
        await message.answer('Имя Фамилия:\nНапример :  "Иванов Сергей"')
        await Form.name_username.set()
    elif message.text == 'Електрик':
        xz_turi = message.text
        async with state.proxy() as data:
            data['service_type'] = message.text
        await message.answer('Имя Фамилия:\nНапример :  "Иванов Сергей"')
        await Form.name_username.set()


@dp.message_handler(state=Form.name_username)
async def rek_photo1(message: types.Message, state: FSMContext):
    if xz_turi in ['Santexnik', 'Elektrik']:
        async with state.proxy() as data:
            data['name_username'] = message.text
        await Form.next()
        await message.answer(
            "Telefon raqamingizni pastdagi tugma orqali kiriting. Yoki shablon orqali  kiriting:\n M-n:  +998 XX XXX XX XX",
            reply_markup=contact1)
    elif xz_turi in ['Сантехник', 'Електрик']:
        async with state.proxy() as data:
            data['name_username'] = message.text
        await Form.next()
        await message.answer(
            "Введите свой номер телефона, используя кнопку ниже.  Или введите через шаблон:\n Например: +998 XX XXX XX XX",
            reply_markup=contact1)


@dp.message_handler(content_types=types.ContentType.CONTACT, state=Form.phone_number)
async def rek_photo(message: types.Message, state: FSMContext):
    if xz_turi in ['Santexnik', 'Elektrik']:
        async with state.proxy() as data:
            data['phone_number'] = message.contact.phone_number
        await Form.next()
        await message.answer('Qisqa izoh kiriting.')
    elif xz_turi in ['Сантехник', 'Електрик']:
        async with state.proxy() as data:
            data['phone_number'] = message.contact.phone_number
        await Form.next()
        await message.answer('Введите короткий комментарий')


@dp.message_handler(state=Form.phone_number)
async def rek_photo(message: types.Message, state: FSMContext):
    if xz_turi in ['Santexnik', 'Elektrik']:
        async with state.proxy() as data:
            phone_number = message.text
            if validate_phone_number(phone_number):
                data['phone_number'] = phone_number
            else:
                await message.answer("Noto'g'ri formatdagi telefon raqamini kiritdingiz. Iltimos, qaytadan kiriting.")
                return
        await Form.next()
        await message.answer('Qisqa izoh kiriting.')
    elif xz_turi in ['Сантехник', 'Електрик']:
        async with state.proxy() as data:
            phone_number = message.text
            if validate_phone_number(phone_number):
                data['phone_number'] = phone_number
            else:
                await message.answer("Вы ввели номер телефона в неправильном формате. Пожалуйста, введите еще раз.")
                return
        await Form.next()
        await message.answer('Введите короткий комментарий')


@dp.message_handler(state=Form.comment)
async def rek_photo(message: types.Message, state: FSMContext):
    if xz_turi in ['Santexnik', 'Elektrik']:
        async with state.proxy() as data:
            data['comment'] = message.text
        await Form.next()
        await message.answer("Pastdagi tugma orqali manzilni yuboring.", reply_markup=key)
    elif xz_turi in ['Сантехник', 'Електрик']:
        async with state.proxy() as data:
            data['comment'] = message.text
        await Form.next()
        await message.answer('Отправьте адрес, используя кнопку ниже.', reply_markup=key1)


@dp.message_handler(state=Form.location, content_types=types.ContentType.LOCATION)
async def rek_photo(location: types.Message, state: FSMContext):
    global loc
    loc = location.location
    global user_id
    user_id = location.from_user.id
    global loc1
    loc1 = location.message_id

    if xz_turi in ['Santexnik', 'Elektrik']:
        async with state.proxy() as data:
            data['location'] = location.location
        global v
        global v2
        v = f"🛑 Ism va Familiya  :   {data['name_username']}\n🛑 Telefon raqam  :   {data['phone_number']}\n🛑 Xizmat turi  :   {data['service_type']}\n🛑 Izoh  :   {data['comment']}\n\n🛑 Ma'lumotlar to'g'riligini tekshiring va pastdagi tugma orqali tasdiqlang."
        v2 = f"📌 Mijoz ma'lumotlari\n\n🛑 Ism va Familiya  :   {data['name_username']}\n🛑 Telefon raqam  :   {data['phone_number']}\n🛑 Xizmat turi  :   {data['service_type']}\n🛑 Izoh  :   {data['comment']}"
        await bot.send_message(user_id, v, reply_markup=keyboard7)
        await state.finish()
    elif xz_turi in ['Сантехник', 'Електрик']:
        async with state.proxy() as data:
            data['location'] = location.location
        global v1
        v1 = f"🛑 Имя и Фамилия  :   {data.get('name_username')}\n🛑 Ваш номер телефона  :   {data.get('phone_number')}\n🛑 Тип услуги  :   {data.get('service_type')}\n🛑 Комментарий  :   {data.get('comment')}\n\n🛑 Проверьте правильность информации и подтвердите ее кнопкой ниже."
        await bot.send_message(user_id, v1, reply_markup=keyboard8)
        await state.finish()


@dp.message_handler(lambda message: message.text in ['Tasdiqlash', 'Ozgartirish', 'Подтверждение', 'Изменять'])
async def rek_photo(message: types.Message, state: FSMContext):
    if message.text == 'Tasdiqlash':
        guruh_chat_id = [-1002119431034, -1002133646301]
        for i in guruh_chat_id:
            await bot.send_location(i, loc.latitude, loc.longitude)
            await bot.send_message(chat_id=i, text=v2)
            await message.answer('Ma\'lumotlar adminga yuborildi', reply_markup=keyboard)
            await state.finish()
    elif message.text == 'Ozgartirish':
        await message.answer('Xizmatni turini tanlang', reply_markup=keyboard4)
        await state.finish()
    elif message.text == 'Подтверждение':
        guruh_chat_id = -1002119431034
        await bot.send_location(guruh_chat_id, loc.latitude, loc.longitude)
        await bot.send_message(chat_id=guruh_chat_id, text=v1)
        await message.answer('Информация отправлена администратору.', reply_markup=keyboard)
        await state.finish()
    elif message.text == 'Изменять':
        await message.answer('Выберите тип услуги', reply_markup=keyboard3)
        await state.finish()


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer('Bizda  bunday buyruq mavjud emas. /  У нас нет такого приказа. ', reply=message.text)


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
