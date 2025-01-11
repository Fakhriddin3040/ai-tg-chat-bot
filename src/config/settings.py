
import os
import dotenv
from django.conf.global_settings import INSTALLED_APPS, DATABASES

dotenv.load_dotenv()

TG_API_KEY = os.environ.get("TG_API_KEY")
AI_API_KEY = os.environ.get("OPEN_AI_API_KEY")

if not TG_API_KEY:
    raise ValueError("TG_API_KEY not set")


INSTALLED_APPS = [
    "src.tg_bot",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'tg_db.sqlite3',
    }
}
