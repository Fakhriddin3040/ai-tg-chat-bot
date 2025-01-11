import django
from django.conf import settings
from django.core.management import call_command

from src.config import settings as local_settings

def makemigrations():
    call_command('makemigrations')

def migrate():
    call_command("migrate")

def configure_orm():
    settings.configure(
        DATABASES=local_settings.DATABASES,
        INSTALLED_APPS=local_settings.INSTALLED_APPS,
    )
    django.setup()
    makemigrations()
    migrate()