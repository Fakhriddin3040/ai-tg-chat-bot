from django.db import models as django_models


class TelegramUser(django_models.Model):
    id = django_models.BigIntegerField(primary_key=True)
    first_name = django_models.CharField(max_length=120)
    last_name = django_models.CharField(max_length=120, null=True)
    username = django_models.CharField(max_length=120, null=True)

    class Meta:
        app_label = "tg_bot"
        indexes = [
            django_models.Index(fields=["tg_id"], name="tg_id_idx"),
        ]