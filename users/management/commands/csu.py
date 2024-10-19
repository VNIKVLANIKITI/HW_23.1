from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email='admin@example.com', first_name= 'Admin', last_name = 'SkyPro')
        user.set_password('123qwe456rty')
        user.is_active = True 
        user.is_staff = True
        user.is_superuser = True
        user.save()
