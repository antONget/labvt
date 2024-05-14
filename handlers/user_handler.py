import logging

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.filters import StateFilter
# from services import googleSheets
from datetime import datetime
from keyboards.user_keyboard import keyboard_start, keyboard_catalog, keyboard_connect, contact_keyboard
import re


router = Router()


class Form(StatesGroup):
    name = State()
    phone = State()


def validate_russian_phone_number(phone_number):
    # Паттерн для российских номеров телефона
    # Российские номера могут начинаться с +7, 8, или без кода страны
    pattern = re.compile(r'^(\+7|8|7)?(\d{10})$')

    # Проверка соответствия паттерну
    match = pattern.match(phone_number)

    return bool(match)


@router.message(CommandStart())
async def press_button_start(message: Message):
    logging.info('')
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    # googleSheets.append_start(message.chat.id, message.chat.username, date)
    keyboard = keyboard_start()
    await message.answer(text="Вас приветствует компания ????? – ведущий российский производитель "
                              "комплектующих и декора для мебели и интерьеров. Самый большой ассортимент на рынке.\n\n"
                              "Познакомьтесь с нашим ассортиментом, скачав каталоги и узнайте выгодное персональное "
                              "предложение для каждой категории клиентов.",
                         reply_markup=keyboard)


@router.callback_query(F.data == "catalog")
async def callback_catalog(callback: CallbackQuery):
    logging.info('callback_catalog')
    await callback.message.answer(text='Выберите каталог и скачайте, нажав на кнопку с его названием',
                                  reply_markup=keyboard_catalog())


@router.callback_query(F.data.startswith("cat_"))
async def callback_catalog_press(callback: CallbackQuery):
    logging.info('callback_catalog')
    description = ['Описание товара "Камерные печи"',
                   'Проходные печи используются для непрерывно протекающих термических процессов обжига.'
                   ' Количество зон туннели и конструкция устройства загрузки зависит от требуемой'
                   ' производительности и параметров термического процесса.\n'
                   'Особенности:\n'
                   '• Температура до 1450 С;\n'
                   '• Специальная зона на выходе из туннели для охлаждения заготовок;\n'
                   '• Несколько зон нагрева с независимым управлением;\n'
                   '• Управление скоростью подачи садки;\n'
                   '• Высокая точность поддержания температуры;\n'
                   '• Модульная конструкция: упрощает доставку и монтаж;\n'
                   '• Архивация процесса.',
                   'Описание товара "Комбинированные решения"']
    photo_id = ['AgACAgIAAxkBAAMTZkOZlOJnnYkNVUFz62uVcdxbZecAAhzhMRtb0BhK6PeupLvIYjgBAAMCAAN5AAM1BA',
                'AgACAgIAAxkBAAMUZkOZzbDsWs7laf72YYga87gHgiEAAh3hMRtb0BhKv4DtPKKiQSQBAAMCAAN5AAM1BA',
                'AgACAgIAAxkBAAMVZkOZ9jTEfmv3OPyeFZ1tCPokPGwAAh7hMRtb0BhKXBobGok5aA0BAAMCAAN5AAM1BA']
    await callback.message.answer_photo(photo=photo_id[int(callback.data.split("_")[1])-1],
                                        caption=f'{description[int(callback.data.split("_")[1])-1]}',
                                        reply_markup=keyboard_connect())

@router.callback_query(F.data == "about_company")
async def callback_sale_company(callback: CallbackQuery):
    logging.info('callback_sale_company')
    # await callback.answer_callback(callback_query_id=callback.id)
    await callback.message.answer(text="О компании")


@router.callback_query(F.data == "connect")
async def callback_connect(callback: CallbackQuery):
    logging.info('callback_connect')
    # callback.answer_callback_query(callback_query_id=callback.id)
    await callback.message.answer(text="У вас возникли вопросы, требуется помощь в подборе моделей декора или вы уже"
                                       " готовы сделать заказ?\n"
                                       "Наши менеджеры рады помочь вам с пн по пт: с 09:00 до 18:00.\n"
                                       "Ваше обращение, оставленное в другое время, не останется без нашего внимания."
                                       " Мы ответим на него в рабочие часы.",
                                  reply_markup=keyboard_connect())


@router.callback_query(F.data == "call_me")
async def callback_connect_call_me(callback: CallbackQuery, state: FSMContext):
    logging.info('callback_connect_call_me')
    # await callback.answer_callback_query(callback_query_id=callback.id)
    await callback.message.answer(text="Укажите свое имя")
    await state.set_state(Form.name)


@router.message(F.text, StateFilter(Form.name))
async def get_contact(message: Message, state: FSMContext):
    # googleSheets.append_name(message.chat.id, message.text)
    # keyboard = keyboards.contact_keyboard()
    await state.update_data(name=message.text)
    await message.answer(text='Укажите ваш номер телефона или поделитесь им через кнопку',
                         reply_markup=contact_keyboard())
    await state.set_state(Form.phone)


@router.message(StateFilter(Form.phone))
async def get_phone_user(message: Message, state: FSMContext) -> None:
    logging.info(f'get_phone_user: {message.chat.id}')
    if message.contact:
        phone = str(message.contact.phone_number)
    else:
        phone = message.text
        if not validate_russian_phone_number(phone):
            await message.answer(text="Неверный формат номера. Повторите ввод:")
            return
    await state.update_data(phone=phone)
    await message.answer(text='Спасибо! Наш менеджер свяжется с Вами в ближайшее время!')

