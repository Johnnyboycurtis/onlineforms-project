from django.db import models
import uuid
from django.contrib.auth.models import User

import random

def rand():
    return random.randint(a=1, b=1000)

SKILL_CHOICES = [('Beginner', 'Beginner'), ('Moderate', 'Moderate'), ('Expert', 'Expert')]


class Dummy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    age = models.CharField(max_length = 100)
    
    class Meta:
        verbose_name_plural = "Dummy"

class Contacts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100, default='something-{}@gmail.com'.format(rand()))
    age = models.IntegerField(default = random.randint(a=22, b=45))
    
    class Meta:
        verbose_name_plural = "Contacts"

class ProgrammingLanguages(models.Model):
    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    skill = models.CharField(max_length = 100, choices = SKILL_CHOICES)

    class Meta:
        verbose_name_plural = "ProgrammingLanguages"

class Sports(models.Model):
    #userid = models.ForeignKey('ContactInfo', on_delete=models.CASCADE)
    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=100, choices = SKILL_CHOICES)

    class Meta:
        verbose_name_plural = "Sports"
