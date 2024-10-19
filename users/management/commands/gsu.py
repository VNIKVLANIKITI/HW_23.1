from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email='guest@mail.ru', first_name= 'Guest', last_name = 'Guest')
        user.set_password('123qwe456rty')
        user.is_active = True 
        user.is_staff = True
        user.is_superuser = True
        user.save()
