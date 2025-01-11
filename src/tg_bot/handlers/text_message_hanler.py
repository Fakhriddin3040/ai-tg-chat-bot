from telegram.ext import filters

from utils.chat_bots.chatgpt4 import chat_bot
from src.tg_bot.services import async_chat_history_service

async def text_message_handler(update, context):
    user = update.effective_user
    user_text = update.message.text
    await async_chat_history_service.acreate(
        user_id=user.id,
        message=user_text,
    )
    response = await chat_bot.send_message(user_text, user_id=user.id)

    await update.message.reply_text(response)

