from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
import logging


def keyboard_start():
    logging.info('keyboard_start')
    button_1 = KeyboardButton(text='О нас')
    button_2 = KeyboardButton(text='Наши продукты')
    button_3 = KeyboardButton(text='Получить консультацию')
    button_4 = KeyboardButton(text='Контакты')
    button_5 = KeyboardButton(text='Часто задаваемые вопросы')
    keyboard = ReplyKeyboardMarkup(keyboard=[[button_1], [button_2], [button_3], [button_4], [button_5]])
    return keyboard


def keyboard_catalog():
    logging.info('keyboard_catalog')
    button_1 = InlineKeyboardButton(text='Муфельные печи', callback_data='product_1')
    button_2 = InlineKeyboardButton(text='Высокотемпературные печи', callback_data='product_2')
    button_3 = InlineKeyboardButton(text='Туннельные печи', callback_data='product_3')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_1], [button_2], [button_3], ])
    return keyboard


def keyboard_connect(product: int):
    logging.info('keyboard_connect')
    button_1 = InlineKeyboardButton(text='Подробнее', callback_data=f'details_{product}')
    button_2 = InlineKeyboardButton(text='Технические характеристики', callback_data=f'tech_{product}')
    button_3 = InlineKeyboardButton(text='Заказать', callback_data=f'order_{product}')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_1], [button_2], [button_3], ])
    return keyboard


def contact_keyboard():
    logging.info('contact_keyboard')
    button_phone = KeyboardButton(text="Отправить телефон", request_contact=True)
    keyboard = ReplyKeyboardMarkup(keyboard=[[button_phone]],
                                   row_width=1,
                                   resize_keyboard=True)
    return keyboard


def keyboard_connect_manager():
    logging.info('keyboard_connect_manager')
    button_1 = InlineKeyboardButton(text='Оставить заявку', callback_data=f'request')
    button_2 = InlineKeyboardButton(text='Отправить контакты', callback_data=f'send_contact')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_1], [button_2],])
    return keyboard


def keyboard_contact_us():
    logging.info('keyboard_contact_us')
    button_1 = InlineKeyboardButton(text='Связаться с нами', callback_data=f'contact_us')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_1],])
    return keyboard


def keyboard_frequently_asked_questions():
    logging.info('keyboard_frequently_asked_questions')
    button_1 = InlineKeyboardButton(text='Оплата и доставка', callback_data=f'pay_and_delivery')
    button_2 = InlineKeyboardButton(text='Гарантия и обслуживание', callback_data=f'warranty_and_service')
    button_3 = InlineKeyboardButton(text='Установка и эксплуатация', callback_data=f'installation_and_operation')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_1], [button_2], [button_3], ])
    return keyboard