from django.apps import AppConfig


class CandidaturaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'candidatura'



class CandidaturaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'candidatura'

    def ready(self):
        import candidatura.signals
