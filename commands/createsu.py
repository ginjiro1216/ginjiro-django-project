from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username="ginjirokinoshita1216").exists():
            User.objects.create_superuser(
                username="ginjirokinoshita1216",
                email="ginjirokinoshita1216@gmail.com",
                password="rQ3EPHSf"
            )
            self.stdout.write(self.style.SUCCESS('Successfully created new super user'))