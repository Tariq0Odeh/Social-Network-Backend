from django.apps import AppConfig


class StoriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stories'

    def ready(self):
        from .delete_story import delete
        delete()

