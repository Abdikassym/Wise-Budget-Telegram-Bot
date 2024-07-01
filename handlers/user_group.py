from string import punctuation

from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from filters.chat_types import ChatTypeFilter

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))


restricted_words = {"чёрт", "кабан", "чмо"}


def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))


@user_group_router.edited_message()
@user_group_router.message()
async def cleaner(message: types.Message):
    if restricted_words.intersection(clean_text(message.text.lower()).split()):
        await message.reply(f"{message.from_user.first_name}, ты сучка, как ты со мной разговариваешь?")
        await message.delete()
