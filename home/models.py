from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to="gallery", blank=False)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return os.path.basename(self.image.name)
    def filename(self):
        return os.path.basename(self.image.name)
@receiver(models.signals.post_delete, sender=Image)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)