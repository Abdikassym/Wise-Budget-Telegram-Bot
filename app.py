import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

URL = f"https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe"


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Это была команда старт.")


@dp.message()
async def echo(message: types.Message, bot: Bot):
    # text = message.text
    # if text in ["Привет!", "привет", "здарова", "дароу", "приветствую", "Привет"]:
    #     await message.answer("И тебе привет!")
    # elif text in ["Пока", "пока", "прощай", "покеда", "до свидания", "сау бол"]:
    #     await message.answer("Пока!")
    # else:
    await message.answer(message.text)
    await message.reply(message.text)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
