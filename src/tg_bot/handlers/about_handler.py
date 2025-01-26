from telegram import Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler, CallbackContext
from src.tg_bot.keyboards.about_company import create_about_company_keyboard


async def about_handler(update: Update, context: CallbackContext) -> None:
    await update.callback_query.answer()

    await update.callback_query.edit_message_text(
        "ㅤㅤㅤㅤㅤㅤㅤㅤ💡Немного про Latoken",
        reply_markup=create_about_company_keyboard()
    )