from django.db import models
import uuid

import random

def rand():
    return random.randint(a=1, b=1000)

SKILL_CHOICES = [('Beginner', 'Beginner'), ('Moderate', 'Moderate'), ('Expert', 'Expert')]

class UserInfo(models.Model):
    userid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100, default='something-{}@gmail.com'.format(rand()))
    age = models.IntegerField(default = random.randint(a=22, b=45))
    
    class Meta:
        verbose_name_plural = "UserInfo"

class ProgrammingLanguages(models.Model):
    userid = models.ForeignKey('UserInfo', on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    skill = models.CharField(max_length = 100, choices = SKILL_CHOICES)

    class Meta:
        verbose_name_plural = "ProgrammingLanguages"

class Sports(models.Model):
    userid = models.ForeignKey('UserInfo', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=100, choices = SKILL_CHOICES)

    class Meta:
        verbose_name_plural = "Sports"
