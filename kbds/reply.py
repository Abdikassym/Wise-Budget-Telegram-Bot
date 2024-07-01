from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Меню"),
            KeyboardButton(text="О нас"),
            KeyboardButton(text="Варианты доставки"),
            KeyboardButton(text="Варианты оплаты"),
        ]
    ]
)
