from django.core.management.base import BaseCommand

from accounts.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("8504041569", "Dark@0404")