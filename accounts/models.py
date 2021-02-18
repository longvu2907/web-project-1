from django.db import models
import os
from django.dispatch import receiver
from uuid import uuid4

def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(path, filename)
    return wrapper

class User(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=15, default="Name")
    password = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to=path_and_rename("avatar"), default="avatar/profile.jpg")
    def __str__(self):
        return self.username
    def filename(self):
        return os.path.basename(self.avatar.name)