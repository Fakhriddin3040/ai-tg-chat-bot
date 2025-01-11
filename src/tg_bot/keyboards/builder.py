from collections.abc import Sequence

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from typing import List, Optional

from src.abstracts.aggregator_builder import AggregateBuilder


class KeyboardBuilder(AggregateBuilder):
    """
    Builder для создания InlineKeyboardMarkup.
    Позволяет пошагово добавлять кнопки и ряды кнопок.
    """

    def __init__(self):
        self.rows: List[List[InlineKeyboardButton]] = []

    def add(
            self,
            text: str,
            callback_data: Optional[str] = None,
            url: Optional[str] = None,
            *args,
            **kwargs
    ) -> 'KeyboardBuilder':
        """
        Добавляет одиночную кнопку в новый ряд.
        """
        button = InlineKeyboardButton(text=text, callback_data=callback_data, url=url, *args, **kwargs)
        self.rows.append([button])
        return self

    def add_row(self, *buttons: List[InlineKeyboardButton]) -> 'KeyboardBuilder':
        """
        Добавляет целый ряд (список) кнопок.
        """
        self.rows.append(*buttons)
        return self

    def build(self) -> InlineKeyboardMarkup:
        """
        Завершает сборку и возвращает InlineKeyboardMarkup.
        """
        return InlineKeyboardMarkup(self.rows)