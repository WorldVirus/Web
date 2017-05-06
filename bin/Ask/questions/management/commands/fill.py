from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from questions.models import Question
from django.core.files import File



class Command(BaseCommand):
    help='fill base'
    def add_arg(self,parser):
        parser.add_arg('-n', action = 'store', dest = 'count', default = 10, help = 'number of users to add')
    def handle(self,*args,**options):
        user=User.objects.get(email='ds@gmail.com')
        for i in range (1,10):
            q=Question(
                author=user,
                text='text'+str(i),
                title='titel'+str(i),
            )
            q.save()
