# handlers/menu_handler.py
from telegram import Update
from telegram.ext import ContextTypes, CallbackQueryHandler
from src.tg_bot.keyboards.main_menu import create_main_menu

async def main_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Команда /menu – показать главное меню
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        "ㅤㅤㅤㅤㅤㅤㅤㅤㅤГлавное меню",
        reply_markup=create_main_menu()
    )
