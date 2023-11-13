import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command
from btn import *


from string import ascii_letters
from random import choice

BOT_TOKEN = "6600379465:AAEf5a5cCTMtJ3HSj1L8Msd94UdK-w1fEoY"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot)


async def command_menu(dp: Dispatcher):
  await dp.bot.set_my_commands(
    [
      types.BotCommand('start', 'Ishga tushirish'),
    ]
  )

async def generate_password(level: str):
  symbols = "!@#$%^&*()*+@#$%^&*()+@#$%"
  numbers = "1234567890"
  password = ""

  if level == "hard_password":
    for i in range(4):
      password += choice(ascii_letters) + choice(symbols) + choice(numbers)
  elif level == "middle_password":
    for i in range(6):
      password += choice(ascii_letters) + choice(numbers)
  else:
    for i in range(8):
      password += choice(numbers)


  return password

@dp.message_handler(commands=['start'])
async def get_start(message:types.Message):
    await message.answer(f"Salom {message.from_user.first_name}", reply_markup=menu)

@dp.message_handler(text="Admin bilan boglanish")
async def admin_handler(message:types.Message):
  await message.answer("Admin: ", reply_markup=admin)

@dp.callback_query_handler(text="admin_telegram")
async def admin_callback(call: types.CallbackQuery):
  await call.message.edit_text(f"<b>Admin telegrami:</b> <code>https://t.me/ikromovabdukhamid</code>")

@dp.callback_query_handler(text="admin_nomeri")
async def admin_callback_number(call: types.CallbackQuery):
  await call.message.edit_text(f"<b>Admin nomeri:</b> <code>+998 94 950 71 73</code>")

@dp.message_handler(text="Parol Yaratish")
async def password_generate(message:types.Message):
  await message.answer("Parol turini tanlang:", reply_markup=password_types)

@dp.callback_query_handler()
async def password_types_callback(call: types.CallbackQuery):
  level = call.data
  password = await generate_password(level)
  await call.message.edit_text(f"<b>Parol:</b> <code>{password}</code>", reply_markup=password_types)




if __name__ == "__main__":
  executor.start_polling(dp, on_startup=command_menu)