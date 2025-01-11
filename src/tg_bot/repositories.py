from src.abstracts.async_repository import AsyncAbstractEditRepository, AsyncAbstractFetchRepository, \
    AsyncAbstractRepository
from src.abstracts.repository import AbstractRepository
from src.tg_bot.models import TelegramUser
from src.tg_bot.models.chat_history import ChatHistory


class TelegramUserRepository(AbstractRepository[TelegramUser]):
    model = TelegramUser


class AsyncTelegramUserRepository(AsyncAbstractEditRepository):
    model = TelegramUser


class ChatHistoryRepository(AbstractRepository[ChatHistory]):
    model = ChatHistory


class AsyncChatHistoryRepository(AsyncAbstractRepository[ChatHistory]):
    model = ChatHistory

telegram_user_repo = TelegramUserRepository()
async_telegram_user_repo = AsyncTelegramUserRepository()

chat_history_repo = ChatHistoryRepository()
async_chat_history_repo = AsyncChatHistoryRepository()