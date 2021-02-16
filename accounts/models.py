from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.username
