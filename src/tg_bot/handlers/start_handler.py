# handlers/start_handler.py
from asgiref.sync import sync_to_async
from telegram import Update
from telegram.ext import ContextTypes
from src.tg_bot.keyboards.main_menu import create_main_menu  # Главное меню
from src.tg_bot.repositories import async_telegram_user_repo
from src.tg_bot.services import async_telegram_user_service, async_chat_history_service


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Хендлер для команды /start.
    Отправляет приветственное сообщение и клавиатуру главного меню.
    """
    user = update.effective_user
    welcome_text = await async_telegram_user_service.get_welcome_msg(user)
    await update.message.reply_text(
        text=welcome_text,
        reply_markup=create_main_menu(),  # Главное меню
    )