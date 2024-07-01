from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from aiogram.enums import ParseMode
from aiogram.utils.formatting import as_list, as_marked_section, Bold

from filters.chat_types import ChatTypeFilter

from kbds import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привет, я виртуальный помощник.", reply_markup=reply.start_kb3.as_markup(
        resize_keyboard=True,
        input_field_placeholder="Что вас интересует?"
    ))


@user_private_router.message(F.text.lower() == "меню")
@user_private_router.message(Command("menu"))
async def menu_cmd(message: types.Message):
    await message.answer("Вот меню: ", reply_markup=reply.del_kbd)


@user_private_router.message(or_f(Command("about"), (F.text.lower() == "о нас")))
async def about_cmd(message: types.Message):
    await message.answer("Это информация про бота:")


@user_private_router.message(or_f(Command("payment"), (F.text.lower().contains("оплат"))))
async def payment_cmd(message: types.Message):
    text = as_marked_section(
        "Варианты оплаты:",
        "Картой в боте",
        "При получении карта/наличные",
        "В заведении",
        marker="✅"
    )
    # await message.answer("<b>Информация о способах оплаты</b>", parse_mode=ParseMode.HTML)
    await message.answer(text.as_html())


# Срабатывает при написании фразы "доставка" в любом формате
@user_private_router.message(or_f(Command("shipping"), (F.text.lower().contains("доставк"))))
async def shipping_cmd(message: types.Message):
    text = as_list(as_marked_section(
        "Варианты доставки/заказа:",
        "Курьер",
        "Самовынос (сейчас прибегу и заберу)",
        "Покушаю у Вас (сейчас прибегу)",
        marker="✅ "
    ),
        as_marked_section(
        "Нельзя:",
        "Почта",
        "Голуби",
        marker="❌ "
    ),
        sep="\n----------------------\n")
    # await message.answer("Информация о видах доставки", reply_markup=reply.test_keyboard)
    await message.answer(text.as_html())


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


@user_private_router.message(F.contact)
async def get_contact(message: types.Message):
    await message.answer(f"номер получен")
    await message.answer(str(message.contact))


@user_private_router.message(F.location)
async def get_location(message: types.Message):
    await message.answer(f"местоположение получено")
    await message.answer(str(message.location))
