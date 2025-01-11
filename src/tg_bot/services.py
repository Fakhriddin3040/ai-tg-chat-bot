from asgiref.sync import sync_to_async, async_to_sync

from src.abstracts.async_service import AsyncAbstractService
from src.abstracts.service import AbstractService
from src.tg_bot.models import TelegramUser
from src.tg_bot.models.chat_history import ChatHistory
from src.tg_bot.repositories import TelegramUserRepository, telegram_user_repo, AsyncTelegramUserRepository, \
    async_telegram_user_repo, ChatHistoryRepository, chat_history_repo, AsyncChatHistoryRepository, \
    async_chat_history_repo


class TelegramUserService(AbstractService[TelegramUser]):
    def __init__(self, repository: TelegramUserRepository = telegram_user_repo):
        super().__init__(repository)



class AsyncTelegramUserService(AsyncAbstractService[TelegramUserService]):
    def __init__(self, repository: AsyncTelegramUserRepository = async_telegram_user_repo):
        super().__init__(repository)

    async def get_welcome_msg(self, tg_user) -> str:
        user_instance, created = await self.aget_or_create(
            id=tg_user.id,
            defaults=dict(
                username=tg_user.username,
                first_name=tg_user.first_name,
                last_name=tg_user.last_name,
            )
        )
        if created:
            return (
                f"Привет, {tg_user.first_name}! Добро пожаловать в мир Latoken.\n\nЯ ваш персональный ассистент."
                "Здесь вы можете общаться с ИИ, узнать о нашей компании, карьерных возможностях, достижениях "
                "и многом другом. Просто выберите одну из опций в главном меню, и мы начнем!"
            )
        return (
            f"Привет, {tg_user.first_name}! Рад вас снова видеть.\n\nЯ ваш персональный ассистент в Latoken. "
            f"Если вам нужно что-то узнать о компании, карьерных возможностях или просто пообщаться с ИИ,"
            "выберите опцию из главного меню."
        )


class ChatHistoryService(AbstractService[ChatHistory]):
    def __init__(self, repository: ChatHistoryRepository = chat_history_repo):
        super().__init__(repository)

    @sync_to_async
    def get_chat_history(self, user_id: int):
        history = self._repository.filter(
            id=user_id,
        ).only("message", "created_at")[:20]
        return "\n\n".join([f"{i}. {h.message}" for i, h in enumerate(history, 1)])



class AsyncChatHistoryService(AsyncAbstractService[ChatHistory]):
    def __init__(self, repository: AsyncChatHistoryRepository = async_chat_history_repo):
        super().__init__(repository)

    @sync_to_async
    def _get_chat_history(self, user_id: int):
        history = self._repository.filter(
            user_id=user_id,
        ).only("message", "created_at")[:20]
        return "\n\n".join([f"{i}. {h.message}" for i, h in enumerate(history, 1)])

    async def get_chat_history(self, user_id: int):
        return await self._get_chat_history(user_id)

telegram_user_service = TelegramUserService()
async_telegram_user_service = AsyncTelegramUserService()

chat_history_service = ChatHistoryService()
async_chat_history_service = AsyncChatHistoryService()
