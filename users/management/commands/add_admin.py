from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = get_user_model()
        user = user.objects.create(
            email='admin@mail.ru',
            username='admin',
            first_name='Andrey',
            last_name='Fedorov'
        )
        user.set_password('12345')
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(self.style.SUCCESS(f'Successfully created admin user with email {user.email}'))