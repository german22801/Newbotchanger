
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from scraper import get_prediction
import os

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton("Показать прогноз"))

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привет! Я помогу предсказать коэффициент в Lucky Jet.", reply_markup=kb)

@dp.message_handler(lambda message: message.text == "Показать прогноз")
async def handle_prediction(message: types.Message):
    await message.answer("Секунду, получаю данные...")
    prediction = get_prediction()
    await message.answer(prediction)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
