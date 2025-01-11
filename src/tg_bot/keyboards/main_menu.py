# keyboards/main_menu.py
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from src.tg_bot.keyboards.builder import KeyboardBuilder
from src.tg_bot.const import CALLBACK_DATA

def create_main_menu() -> InlineKeyboardMarkup:
    kb = KeyboardBuilder()
    kb.add(
        text="🏢 О компании", callback_data=CALLBACK_DATA.ABOUT_COMPANY,
    ).add(
        text="🚀 О хакатоне", callback_data=CALLBACK_DATA.ABOUT_HACKATHON,
    ).add(
        text="🎤 Процесс интервью", callback_data=CALLBACK_DATA.INTERVIEW_PROCESS
    ).add(
        text="🎨 Culture Deck", callback_data=CALLBACK_DATA.CULTURE_DECK
    ).add(
        text="📰 Новости компании", callback_data=CALLBACK_DATA.NEWS
    )# ).add(
    #
    # )
    return kb.build()
