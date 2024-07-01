from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from filters.chat_types import ChatTypeFilter

from kbds import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привет, я виртуальный помощник.", reply_markup=reply.start_kb)


@user_private_router.message(F.text.lower() == "меню")
@user_private_router.message(Command("menu"))
async def menu_cmd(message: types.Message):
    await message.answer("Вот меню: ")


@user_private_router.message(or_f(Command("about"), (F.text.lower() == "о нас")))
async def about_cmd(message: types.Message):
    await message.answer("Это информация про бота:")


@user_private_router.message(or_f(Command("payment"), (F.text.lower() == "оплата")))
async def payment_cmd(message: types.Message):
    await message.answer("Информация о способах оплаты")


# Срабатывает при написании фразы "доставка" в любом формате
@user_private_router.message(or_f(Command("shipping"), (F.text.lower() == "доставка")))
async def shipping_cmd(message: types.Message):
    await message.answer("Информация о видах доставки")


# Срабатывает при отправлении фото
@user_private_router.message(F.photo)
async def magic_filter_cmd(message: types.Message):
    await message.answer("Это магический фильтр фото.")


# Срабатывает при содержании какого-либо текста с содержанием фразы "магический фильтр"
@user_private_router.message(F.text.lower().contains("магический фильтр"))
async def magic_filter_cmd(message: types.Message):
    await message.answer("Это объяснение магического фильтра.")


# Комбинирование выражении, в оодном хендлере можно записать несколько условий
@user_private_router.message((F.text.lower().contains("маг")) & (F.text.lower().contains("фильтр")))
async def combined_magic_filter_cmd(message: types.Message):
    await message.answer("Это комбинированный магический фильтр.")


# Можно комбинировать декораторы чтобы одни не создавать повторение кода для отловки одних и тех же фраз
@user_private_router.message((F.text.contains("декор")) & F.text.contains("дв"))
@user_private_router.message(Command("magic"))
async def double_decorated_magic_filter_cmd(message: types.Message):
    await message.answer("Это дважды декорированный магический фильтр.")
