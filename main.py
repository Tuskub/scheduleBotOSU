import aiogram
from aiogram import Bot, types
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text

import logging, re
import time

from configure import BOT_TOKEN
import key as kb

from src.search.search import Search

logging.basicConfig(level=logging.INFO)

# Инициализируем бота и диспетчера
bot = aiogram.Bot(token=BOT_TOKEN)
dp = aiogram.Dispatcher(bot)

# Обработка команды help
help_message = text("Бот предоставляет расписание занятий:\n"
                    "● студента по номеру его группы (пример: 16КБ(с)РЗПО);\n"
                    "● преподавателя по ФИО (пример: Иванов Иван Иванович);\n"
                    "Реализован выбор отображения расписания:\n"
                    "- на день;\n"
                    "- на неделю;\n"
                    "Функция оповещения позволяет настроить бота для напоминания о занятиях в университете.\n\n"
                    "Доступные команды:\n"
                    "/start - Запуск бота. Выбор роли студент/преподаватель\n"
                    "/notification - Настройка оповещений\n"
                    "/help - Помощь. Краткое руководство по использованию бота"
                    )


@dp.callback_query_handler(lambda c: c.data == 'btn_back')
async def callback_button_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Выберите', reply_markup=kb.inline_kb_main)


@dp.callback_query_handler(lambda c: c.data == 'btn_student')
async def callback_button_student(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Введите номер группы')


@dp.callback_query_handler(lambda c: c.data == 'btn_teacher')
async def callback_button_teacher(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Введите ФИО')


@dp.message_handler(commands=['start'], state="*")
async def command_start(msg: aiogram.types.Message):
    await msg.answer("Вас приветствует schedule_osu_bot!\n", reply_markup=kb.inline_kb_role)


@dp.message_handler(commands=['help'], state="*")
async def command_help(msg: aiogram.types.Message):
    await msg.answer(help_message)


# Вывод команды /mode - будет изменено
@dp.message_handler(commands=['mode'])
async def command_mode(msg: aiogram.types.Message):
    await msg.answer("Выбор вида расписания", reply_markup=kb.inline_kb_mode)


@dp.message_handler(commands=['notification'])
async def command_notif(msg: aiogram.types.Message):
    await bot.send_message(msg.from_user.id,
                           "Здесь нужно обсудить как правильно все настроить и реализовать выбор дней")


# Выдача информации при отправке юзвером любого сообщения
@dp.message_handler(content_types=ContentType.ANY)
async def any_types_send(msg: aiogram.types.Message):
    full_name = msg.text.split(' ')
    surname = full_name[0]
    if surname == 'куз':
        time.sleep(15)
    name = '' if len(full_name) < 2 else full_name[1]
    patronymic = '' if len(full_name) < 3 else full_name[2]
    test = Search()
    teachers = test.teachers_by_name(name, surname, patronymic)
    await bot.send_message(msg.from_user.id, teachers)
    # await bot.send_message(msg.from_user.id, '😐 Неизвестный запрос!\n'
    #                                          'Воспользуйтесь /help')


if __name__ == '__main__':
    # 123
    aiogram.executor.start_polling(dp)
