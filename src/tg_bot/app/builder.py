from typing import Sequence, MutableSequence
from telegram.ext._handlers.basehandler import BaseHandler
from telegram.ext._utils.types import HandlerCallback

from src.abstracts.aggregator_builder import AggregateBuilder
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext, ApplicationBuilder, \
    CallbackQueryHandler


class TelegramApplicationBuilder(AggregateBuilder):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.app = ApplicationBuilder().token(api_key).build()
        self.handlers: MutableSequence[BaseHandler] = []

    def add_command_handler(self, name: str, handler: HandlerCallback, **kwargs):
        self.handlers.append(CommandHandler(name, handler, **kwargs))

    def add_callback_query_handler(self, callback: HandlerCallback, pattern: str = None, **kwargs):
        self.handlers.append(CallbackQueryHandler(callback, pattern=pattern, **kwargs))

    def add_message_handler(self, handler: HandlerCallback, **kwargs):
        self.handlers.append(MessageHandler(filters.TEXT & ~filters.COMMAND, handler, **kwargs))

    def build(self):
        for handler in self.handlers:
            self.app.add_handler(handler)
        return self

    def run(self):
        self.app.run_polling()
        return self