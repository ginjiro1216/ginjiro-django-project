from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    # todo ここで指定する。
    # def add_arguments(self, parser):
    #     parser.add_argument('')

    def handle(self, *args, **options):
        if not User.objects.filter(username="ginjirokinoshita1216").exists():
            User.objects.create_superuser(
                username="ginjirokinoshita1216",
                email="ginjirokinoshita1216@gmail.com",
                password="gingin1216",
            )
            self.stdout.write(
                self.style.SUCCESS("Successfully created new super user")
            )
