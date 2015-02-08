from django.core.management.base import BaseCommand
from django.db import models


class Command(BaseCommand):
    """Prints all models and count of objects in stderr"""
    def handle(self, *args, **options):
        for model in models.get_models(include_auto_created=True):
            self.stderr.write('error: ' + model.__name__ + ' ' + str(model.objects.count()) + '\n')