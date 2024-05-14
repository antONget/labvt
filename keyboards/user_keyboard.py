from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
import logging


def keyboard_start():
    logging.info('keyboard_start')
    button_1 = InlineKeyboardButton(text='О компании', callback_data='about_company')
    button_2 = InlineKeyboardButton(text='Каталог', callback_data='catalog')
    button_3 = InlineKeyboardButton(text='Связаться с менеджером', callback_data='connect')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_1], [button_2], [button_3]])
    return keyboard


def keyboard_catalog():
    logging.info('keyboard_catalog')
    key_1 = InlineKeyboardButton(text='Камерные печи', callback_data='cat_1')
    key_2 = InlineKeyboardButton(text='Туннельные печи', callback_data='cat_2')
    key_3 = InlineKeyboardButton(text='Комбинированные решения', callback_data='cat_3')
    # key_4 = InlineKeyboardButton(text='Каталог 4', callback_data='cat_4')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[key_1], [key_2], [key_3], ])  # наша клавиатура
    return keyboard


def keyboard_connect():
    logging.info('keyboard_connect')
    button_1 = InlineKeyboardButton(text='Написать в телеграм', url='https://t.me/+79214313552')
    button_2 = InlineKeyboardButton(text='Написать в whatsapp', url='https://wa.me/79215791235?'
                                                                          'text=%D0%9F%D0%B8%D1%88%D1%83%20%D0%B2%D0%B0%D0%BC%20%D0%B8%D0%B7%20%D0%B1%D0%BE%D1%82%D0%B0%20stavros!')
    button_3 = InlineKeyboardButton(text='Заказать обратный звонок', callback_data='call_me')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_1], [button_2], [button_3], ])  # наша клавиатура
    return keyboard


def contact_keyboard():
    logging.info('contact_keyboard')
    button_phone = KeyboardButton(text="Отправить телефон", request_contact=True)
    keyboard = ReplyKeyboardMarkup(keyboard=[[button_phone]],
                                   row_width=1,
                                   resize_keyboard=True)
    return keyboard


def keyboard_catalog_finish():
    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_sale = types.InlineKeyboardButton(text='Скидка для вас', callback_data='sale')
    key_connect = types.InlineKeyboardButton(text='Связаться с менеджером', callback_data='connect')
    keyboard.add(key_sale, key_connect)
    return keyboard

def keyboard_sale():
    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_dizainer = types.InlineKeyboardButton(text='Дизайнер', callback_data='dizainer')
    key_stolyr = types.InlineKeyboardButton(text='Столярная мастерская/строительство', callback_data='stolyr')
    key_cpmpany = types.InlineKeyboardButton(text='Мебельная компания', callback_data='company')
    key_mebel = types.InlineKeyboardButton(text='Крупная мебельная фабрика', callback_data='mebel')
    key_diler = types.InlineKeyboardButton(text='Торгующая организация/дилер', callback_data='diler')
    key_chastnik = types.InlineKeyboardButton(text='Частное лицо', callback_data='chastnik')
    keyboard.add(key_dizainer)
    keyboard.add(key_stolyr)
    keyboard.add(key_cpmpany)
    keyboard.add(key_mebel)
    # keyboard.add(key_diler)
    keyboard.add(key_chastnik)
    return keyboard


def keyboard_sale_v1():
    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_catalog = types.InlineKeyboardButton(text='Отправить цифру', url='https://t.me/stsavros')
    keyboard.add(key_catalog)
    return keyboard


def keyboard_sale_finish():
    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_catalog = types.InlineKeyboardButton(text='Скачать каталог', callback_data='catalog')
    key_connect = types.InlineKeyboardButton(text='Связаться с менеджером', callback_data='connect')
    keyboard.add(key_catalog, key_connect)
    return keyboard






