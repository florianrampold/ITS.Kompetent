from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    verbose_name = "Benutzer-Einstellung"
    verbose_name_plural = "Benutzer-Einstellungen"
