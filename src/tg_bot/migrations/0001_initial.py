# Generated by Django 5.1.4 on 2025-01-11 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('tg_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120, null=True)),
                ('username', models.CharField(max_length=120, null=True)),
            ],
            options={
                'db_table': 'telegram_user',
                'indexes': [models.Index(fields=['tg_id'], name='tg_id_idx')],
            },
        ),
    ]
