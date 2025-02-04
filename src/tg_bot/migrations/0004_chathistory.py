# Generated by Django 5.1.4 on 2025-01-11 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg_bot', '0003_alter_telegramuser_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_history', to='tg_bot.telegramuser', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'История чата',
                'verbose_name_plural': 'Истории чатов',
                'ordering': ['-created_at'],
                'indexes': [models.Index(fields=['created_at', 'user'], name='tg_bot_chat_created_86a8ac_idx')],
            },
        ),
    ]
