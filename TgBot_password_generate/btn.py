from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.row("Parol Yaratish")
menu.row("Admin bilan boglanish")

password_types = InlineKeyboardMarkup(row_width=1)

password_types.add(
    InlineKeyboardButton(text="Murakkab", callback_data="hard_password"),
    InlineKeyboardButton(text="O`rtacha", callback_data="middle_password"),
    InlineKeyboardButton(text="Oddiy", callback_data="easy_password")

)

admin = InlineKeyboardMarkup(row_width=1)

admin.add(
    InlineKeyboardButton(text="Admin telegrami", callback_data="admin_telegram"),
    InlineKeyboardButton(text="Admin nomeri", callback_data="admin_nomeri")
)