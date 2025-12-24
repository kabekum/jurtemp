from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
    verbose_name = "myapp" # change the app name in admin panel
    
    def ready(self):
        import myapp.signals  # register signals
