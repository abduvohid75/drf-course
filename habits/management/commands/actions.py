from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='akkafzala1@gmail.com',
            first_name='Admin',
            last_name='Admin',
            is_staff=True,
            is_superuser=True,
        )

        user.set_password('123password456')
        user.save()
