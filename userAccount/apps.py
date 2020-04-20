from django.apps import AppConfig


class UserAccountConfig(AppConfig):
    name = 'userAccount'


    def ready(self):
        import userAccount.signals