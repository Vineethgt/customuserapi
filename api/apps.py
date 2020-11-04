from django.apps import AppConfig
from api import signals


class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        import api.signals
