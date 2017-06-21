from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):
        #if your reading this, it's not my real password ;)
        my_user = User.objects.create_superuser(username='lindsay', password='123', email='lindsayloughlin@gmail.com')
        print('Create admin user')
        my_user.save()


