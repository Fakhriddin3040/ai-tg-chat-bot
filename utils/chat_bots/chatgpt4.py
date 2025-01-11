from typing import List, Dict

from asgiref.sync import sync_to_async

from src.tg_bot.services import telegram_user_service, chat_history_service, async_chat_history_service

# from src.abstracts.ai_api_interface import AIApiInterface


chat_bot_default = """
    Ты чат-бот помощник для пользователей Телеграма, и ты должен помогать им в их запросах.
    Тема - только про Latoken, и ничего кроме. Если пользователь спрашивает о чем-то другом, ты должен сказать, что не можешь помочь.
    Не надо спрашивать, есть ли у него другие вопросы. Можешь попросить его, рассказать о чём-то связанным с твоим ответом.
    Необходимо быть вежливым и уважительным.
    Ответ с Markdown, если Telegram это поддерживает.
    Необходимо быть грамотным, но не стоит употреблять сложные слова.
    Необходимо быть корректным и не оскорблять собеседника.
    Необходимо быть дружелюбным и отзывчивым.
    Ниже, тебе будут передаваться история с текущим пользователем. 
"""

class ChatGPT4o:
    def __init__(self, api_key: str):
        import openai
        self.openai = openai
        self.set_api_key(api_key)
        self.chat_history_service = async_chat_history_service

    def set_api_key(self, api_key: str):
        """ Устанавливает API ключ для взаимодействия с OpenAI. """
        self.openai.api_key = api_key

    async def send_message(
            self,
            user_message: dict | str,
            user_id: int,
            temperature: float = 1,
            max_tokens: int = 500,
            **kwargs
    ) -> str:
        # Формируем дефолтное сообщение с правилами и историей
        history = await self.chat_history_service.get_chat_history(user_id)
        if isinstance(user_message, str):
            user_message = {"role": "user", "content": user_message}

        messages = [
            {"role": "system", "content": chat_bot_default},
            {"role": "user", "content": f"History: {history or ""}"},
            user_message
        ]
        print(history)
        response = self.openai.ChatCompletion.create(
            model="gpt-4",  # Используем модель GPT-4
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            **kwargs
        )

        return response['choices'][0]['message']['content']
OPENAI_API_KEY='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'

chat_bot = ChatGPT4o(OPENAI_API_KEY)
