from src.tg_bot.const import CALLBACK_DATA, HELP_URLS
from src.tg_bot.keyboards.main_menu import create_main_menu
from src.tg_bot.repositories import AsyncChatHistoryRepository
from src.tg_bot.services import TelegramUserService, AsyncTelegramUserService, async_telegram_user_service, \
    async_chat_history_service, AsyncChatHistoryService
from utils.chat_bots.chatgpt4 import ChatGPT4o, chat_bot


class EndpointsHandler:
    def __init__(
            self,
            chat_bot: ChatGPT4o = chat_bot,
            user_service: AsyncTelegramUserService = async_telegram_user_service,
            chat_history_service: AsyncChatHistoryService = async_chat_history_service
    ):
        self.chat_bot = chat_bot
        self.user_service = user_service
        self.chat_history_service = chat_history_service

    async def handle(self, update, context):
        query = update.callback_query
        query.answer()

        callback_data = query.data
        print(10*"-", f"\nCallback-data: {callback_data}\n", 10*"-")
        user_id = update.effective_user.id
        url = HELP_URLS.get(callback_data)

        helpfull_url = {
            "role": "system",
            "content": f"Тут несколько дополнительных ссылок, чтоб ты их изучил для ответа."
                       f"Если ссылок нет, импровизируй.\n\nUrls: {url}. На всякий случай, тут callback data: {callback_data}(Ну триггер, типо нажатая кнопака)."
        }

        await self.chat_history_service.acreate(
            user_id=user_id,
            message=f"Пользователь нажал на кнопку {callback_data}, и тебе были даны ссылки и текст для изучения: {url}"
        )
        response = await self.chat_bot.send_message(helpfull_url, user_id)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(
            "*Главное меню*",
            reply_markup=create_main_menu()
        )

