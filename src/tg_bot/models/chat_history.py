from django.db import models
from .user import TelegramUser


class ChatHistory(models.Model):
    """
    Модель истории чата.
    """
    user = models.ForeignKey(
        TelegramUser,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='chat_history',
    )
    message = models.TextField(
        verbose_name='Сообщение',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )

    class Meta:
        ordering = ['created_at']
        verbose_name = 'История чата'
        verbose_name_plural = 'Истории чатов'
        indexes = [
            models.Index(fields=['created_at', 'user']),
        ]

    def __str__(self):
        return f'{self.user} - {self.created_at}'