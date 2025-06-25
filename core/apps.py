from django.apps import AppConfig
from data_scraping.settings import SCHEDULER_AUTOSTART


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"

