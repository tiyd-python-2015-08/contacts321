from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Contact(models.Model):
    owner = models.ForeignKey(User, related_name='contacts')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
