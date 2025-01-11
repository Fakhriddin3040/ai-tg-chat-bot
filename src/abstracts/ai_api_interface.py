from abc import ABC, abstractmethod
from typing import List, Dict

class AIApiInterface(ABC):
    @abstractmethod
    def send_message(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """
        Отправляет сообщение в модель и возвращает ответ.
        :param messages: Список сообщений (контекста общения).
        :param kwargs: Дополнительные параметры (например, temperature, max_tokens).
        :return: Ответ от модели.
        """
        pass

    @abstractmethod
    def set_api_key(self, api_key: str):
        """
        Устанавливает API ключ для работы с моделью.
        :param api_key: API ключ.
        """
        pass
