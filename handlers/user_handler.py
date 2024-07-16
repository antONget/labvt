import logging

from aiogram import Router, F, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.filters import StateFilter

from keyboards.user_keyboard import keyboard_start, keyboard_catalog, keyboard_connect, contact_keyboard,\
    keyboard_connect_manager, keyboard_contact_us
from filter.user_filter import validate_russian_phone_number
from config_data.config import Config, load_config

router = Router()
config: Config = load_config()

class Form(StatesGroup):
    name = State()
    phone = State()


@router.message(CommandStart())
async def press_button_start(message: Message):
    logging.info('press_button_start')
    await message.answer(text="Вас приветствует компания ????? – ведущий российский производитель "
                              "комплектующих и декора для мебели и интерьеров. Самый большой ассортимент на рынке.\n\n"
                              "Познакомьтесь с нашим ассортиментом, скачав каталоги и узнайте выгодное персональное "
                              "предложение для каждой категории клиентов.",
                         reply_markup=keyboard_start())


# 1
@router.message(F.text == 'Наши продукты')
async def press_catalog(message: Message):
    logging.info('press_catalog')
    await message.answer(text='Выберите продукцию',
                         reply_markup=keyboard_catalog())


@router.callback_query(F.data.startswith("product_"))
async def callback_catalog_press(callback: CallbackQuery, state: FSMContext):
    """
    Выводим информацию по выбранному продукту
    :param callback:
    :param state:
    :return:
    """
    logging.info('callback_catalog')
    await state.update_data(product=callback.data.split("_")[1])
    description = ['Описание товара "Муфельные печи"',
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
                   'Описание товара "Высокотемпературные печи"',
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
                   'Описание товара "Туннельные печи"',
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
                   '• Архивация процесса.']
    photo_id = ['AgACAgIAAxkBAAMTZkOZlOJnnYkNVUFz62uVcdxbZecAAhzhMRtb0BhK6PeupLvIYjgBAAMCAAN5AAM1BA',
                'AgACAgIAAxkBAAMUZkOZzbDsWs7laf72YYga87gHgiEAAh3hMRtb0BhKv4DtPKKiQSQBAAMCAAN5AAM1BA',
                'AgACAgIAAxkBAAMVZkOZ9jTEfmv3OPyeFZ1tCPokPGwAAh7hMRtb0BhKXBobGok5aA0BAAMCAAN5AAM1BA']
    await callback.message.answer_photo(photo=photo_id[int(callback.data.split("_")[1])-1],
                                        caption=f'{description[int(callback.data.split("_")[1])-1]}',
                                        reply_markup=keyboard_connect(product=int(callback.data.split("_")[1])))


@router.callback_query(F.data.startswith("details_"))
async def callback_catalog_press(callback: CallbackQuery):
    logging.info('callback_catalog')
    list_product = ['Муфельные печи', 'Высокотемпературные печи', 'Туннельные печи']
    num_product = int(callback.data.split('_')[1]) - 1
    await callback.message.answer(text=f'Подробнее о продукте: {list_product[num_product]}')


@router.callback_query(F.data.startswith("tech_"))
async def callback_catalog_press(callback: CallbackQuery):
    logging.info('callback_catalog')
    list_product = ['Муфельные печи', 'Высокотемпературные печи', 'Туннельные печи']
    num_product = int(callback.data.split('_')[1]) - 1
    await callback.message.answer(text=f'Технические характеристики продукта: {list_product[num_product]}')


@router.callback_query(F.data.startswith("order_"))
async def callback_catalog_press(callback: CallbackQuery, bot: Bot):
    logging.info('callback_catalog')
    list_product = ['Муфельные печи', 'Высокотемпературные печи', 'Туннельные печи']
    num_product = int(callback.data.split('_')[1]) - 1
    try:
        await bot.send_message(chat_id=config.tg_bot.admin_ids,
                               text=f'Пользователь @{callback.from_user.username} хочет заказать продукт:'
                                    f' {list_product[num_product]}')
    except:
        pass
    await callback.message.answer(text=f'Информация направлена менеджеру')

# 2
@router.message(F.text == 'О нас')
async def about_company(message: Message):
    logging.info('about_company')
    await message.answer(text="О нас: более подробная информация о компании (наши преимущества, история компании)")


# 3
@router.message(F.text == 'Получить консультацию')
async def about_company(message: Message):
    logging.info('about_company')
    await message.answer(text="Вы можете оставить заявку и вам откроется диалог с нашим специалистом, либо оставить"
                              " контакты и он свяжется с вами в ближайшее время.",
                         reply_markup=keyboard_connect_manager())


@router.callback_query(F.data == "request")
async def callback_request(callback: CallbackQuery):
    logging.info('callback_request')
    await callback.message.answer(text="открывается диалог со специалистом\n\n"
                                       "нужен usrname специалиста")


@router.callback_query(F.data == "send_contact")
async def callback_connect_call_me(callback: CallbackQuery, state: FSMContext):
    logging.info('callback_send_contact')
    await callback.message.answer(text='Укажите ваш номер телефона или поделитесь им через кнопку',
                                  reply_markup=contact_keyboard())
    await state.set_state(Form.phone)


@router.message(StateFilter(Form.phone))
async def get_phone_user(message: Message, state: FSMContext, bot: Bot) -> None:
    logging.info(f'get_phone_user: {message.chat.id}')
    if message.contact:
        phone = str(message.contact.phone_number)
        try:
            await bot.send_message(chat_id=config.tg_bot.admin_ids,
                                   text=f'Поступила заявка на консультацию. Номер телефона: {phone}')
        except:
            await bot.send_message(chat_id=config.tg_bot.admin_ids,
                                   text=f'Поступила заявка на консультацию. Номер телефона: {phone}')
    else:
        phone = message.text
        if not validate_russian_phone_number(phone):
            await message.answer(text="Неверный формат номера. Повторите ввод:")
            return
        else:
            try:
                await bot.send_message(chat_id=config.tg_bot.admin_ids,
                                       text=f'Поступила заявка на консультацию. Номер телефона: {phone}')
            except:
                await bot.send_message(chat_id=config.tg_bot.admin_ids,
                                       text=f'Поступила заявка на консультацию. Номер телефона: {phone}')
    await message.answer(text='Спасибо! Наш менеджер свяжется с Вами в ближайшее время!',
                         reply_markup=keyboard_start())
    await state.set_state(default_state)


# 4
@router.message(F.text == 'Контакты')
async def contact_company(message: Message):
    logging.info('contact_company')
    await message.answer(text="Контактная информация компании (телефон, email, адрес, ссылки на социальные сети).",
                         reply_markup=keyboard_contact_us())


@router.callback_query(F.data == "contact_us")
async def callback_connect_call_me(callback: CallbackQuery):
    logging.info('callback_send_contact')
    await callback.message.answer(text='Информация как с связаться')


# 5
@router.message(F.text == 'Часто задаваемые вопросы')
async def аrequently_asked_questions(message: Message):
    logging.info('аrequently_asked_questions')
    await message.answer(text="Выберите раздел",
                         reply_markup=keyboard_contact_us())


@router.callback_query(F.data == "pay_and_delivery")
async def callback_connect_call_me(callback: CallbackQuery):
    logging.info('callback_send_contact')
    await callback.message.answer(text='Информация об оплате и доставке')


@router.callback_query(F.data == "warranty_and_service")
async def callback_connect_call_me(callback: CallbackQuery):
    logging.info('callback_send_contact')
    await callback.message.answer(text='Информация о гарантии и обслуживании')


@router.callback_query(F.data == "installation_and_operation")
async def callback_connect_call_me(callback: CallbackQuery):
    logging.info('callback_send_contact')
    await callback.message.answer(text='Информация об установке и эксплуатации')