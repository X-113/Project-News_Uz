from django.apps import AppConfig


class InfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'info'

    def ready(self):
        from .signals import contact_signal
        # from .signals import test_signal,subs_signal,news_signal





