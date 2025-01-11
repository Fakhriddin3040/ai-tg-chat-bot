from typing import Sequence

from src.tg_bot.keyboards.builder import KeyboardBuilder
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from src.tg_bot.const import CALLBACK_DATA


def create_about_company_keyboard() -> InlineKeyboardMarkup:
    kb = KeyboardBuilder()
    return kb.add(
        text="🌍 Цель компании", callback_data=CALLBACK_DATA.PURPOSE
    ).add(
        text="🏆 Достижения", callback_data=CALLBACK_DATA.ACHIEVEMENTS
    ).add(
        text="📈 Карьерные возможности", callback_data=CALLBACK_DATA.OPPORTUNITIES
    ).add(
        text="Главное меню", callback_data=CALLBACK_DATA.MAIN_MENU
    ).build()

