from django.apps import AppConfig


class EnsembledAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ensembled_app'
