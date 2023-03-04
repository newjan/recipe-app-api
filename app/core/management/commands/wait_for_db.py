"""
Django command to wait for the database to be available.
"""
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django comamnd to wait for database"""

    def handle(self, *args, **options):
        pass