from django.db import models

# Create your models here.

from django.db import models

import random

def rand():
    return random.randint(a=1, b=1000)

SKILL_CHOICES = [('Beginner', 'Beginner'), ('Moderate', 'Moderate'), ('Expert', 'Expert')]

class UserInfo(models.Model):
    id = models.UUIDField(primary_key=True, default='00{}'.format(rand()), editable=False)
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100, default='something-{}@gmail.com'.format(rand()))
    age = models.IntegerField(default = random.randint(a=22, b=45))

class ProgrammingLanguages(models.Model):
    id = models.ForeignKey('UserInfo', on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    skill = models.CharField(max_length = 100, choices = SKILL_CHOICES)

class Sports(models.Model):
    id = models.ForeignKey('UserInfo', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=100, choices = SKILL_CHOICES)
