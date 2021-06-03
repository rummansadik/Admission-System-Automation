from django.apps import AppConfig


class LoginSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'login_system'

    def ready(self) -> None:
        import login_system.signals
        return super().ready()