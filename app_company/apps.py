from django.apps import AppConfig


class AppCompanyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_company'

    def ready(self):
        import app_company.signals