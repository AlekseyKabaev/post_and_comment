from django.core.management import BaseCommand

from datetime import date

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        login = 'admin'
        password = '123qwert'
        birth_date = date.fromisoformat('2000-02-11')

        # Создаем суперпользователя
        user = User.objects.create(login=login, birth_date=birth_date)

        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(self.style.SUCCESS(f"Суперпользователь {login} был создан."))
