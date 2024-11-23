import logging
import asyncio
import sqlite3

from aiogram import Bot, Dispatcher, types, F
from aiogram.types import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from aiogram import Router

router = Router()
bot = Bot(token='7839930317:AAFnKEP-rraQdaEZ8M0LZMS21qW4D8YYxWE')
dp = Dispatcher()

command = [BotCommand(command="start", description="Начать")]

buttons = [
    [KeyboardButton(text="Добавить задачу"), KeyboardButton(text="Показать задачи")],
    [KeyboardButton(text="Очистить список")],
]
keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, input_field_placeholder="Выберите кнопку")

inline_button = [
    [InlineKeyboardButton(text="Подтвердить", callback_data="confirm_clear")],
    [InlineKeyboardButton(text="Отменить", callback_data="cancel_clear")],
]
inline_keyboard = InlineKeyboardMarkup(inline_keyboard=inline_button)

connect = sqlite3.connect("to_do_list.db")
cursor = connect.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_user INTEGER UNIQUE
)
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (id)
)
"""
)
connect.commit()

def register_user(telegram_user):
    cursor.execute("INSERT OR IGNORE INTO users (telegram_user) VALUES (?)", (telegram_user,))
    connect.commit()

def add_task(telegram_user, task):
    cursor.execute("SELECT id FROM users WHERE telegram_user = ?", (telegram_user,))
    user_id = cursor.fetchone()
    if user_id:
        cursor.execute("INSERT INTO tasks (task, user_id) VALUES (?, ?)", (task, user_id[0]))
        connect.commit()

def get_tasks(telegram_user):
    cursor.execute(
        """
        SELECT tasks.id, tasks.task 
        FROM tasks 
        JOIN users ON tasks.user_id = users.id 
        WHERE users.telegram_user = ?
        """,
        (telegram_user,),
    )
    return cursor.fetchall()

def delete_all_tasks(telegram_user):
    cursor.execute(
        """
        DELETE FROM tasks WHERE user_id = (
            SELECT id FROM users WHERE telegram_user = ?
        )
        """,
        (telegram_user,),
    )
    connect.commit()

def tasks_buttons(tasks):
    markup = InlineKeyboardMarkup()
    for task_id, task_text in tasks:
        button_text = " ".join(task_text.split()[:2])
        markup.add(InlineKeyboardButton(text=button_text, callback_data=f"task_{task_id}"))
    return markup

@router.message(CommandStart())
async def command_start(message: types.Message):
    register_user(message.from_user.id)
    await message.answer(f"Привет, {message.from_user.first_name}!", reply_markup=keyboard)

@router.message(F.text == "Добавить задачу")
async def ask_task(message: types.Message):
    await message.answer("Введите содержание задачи:")

@router.message(lambda msg: msg.text not in ["Добавить задачу", "Показать задачи", "Очистить список"])
async def save_task(message: types.Message):
    add_task(message.from_user.id, message.text)
    await message.answer("Задача добавлена!", reply_markup=keyboard)

@router.message(F.text == "Показать задачи")
async def show_tasks(message: types.Message):
    tasks = get_tasks(message.from_user.id)
    if tasks:
        await message.answer("Ваши задачи:", reply_markup=tasks_buttons(tasks))
    else:
        await message.answer("Список задач пуст.")

@router.message(F.text == "Очистить список")
async def confirm_clear_list(message: types.Message):
    await message.answer("Вы уверены?", reply_markup=inline_keyboard)

@router.callback_query(F.data == "confirm_clear")
async def clear_tasks(callback: types.CallbackQuery):
    delete_all_tasks(callback.from_user.id)
    await callback.message.edit_text("Список задач очищен.", reply_markup=keyboard)

@router.callback_query(F.data == "cancel_clear")
async def cancel_clear(callback: types.CallbackQuery):
    await callback.message.edit_text("Очистка отменена.", reply_markup=keyboard)

async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_router(router)
    await bot.set_my_commands(command)
    await dp.start_polling(bot)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Выход")
