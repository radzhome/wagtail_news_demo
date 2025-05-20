from django.apps import AppConfig


class UtilsConfig(AppConfig):
    default_auto_field: str = "django.db.models.AutoField"
    name = "wagtail_news_demo.utils"
    label = "utils"
