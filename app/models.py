from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.

class UploadFile(models.Model):
	file = models.FileField(upload_to='')

@receiver(post_delete, sender=UploadFile)
def delete_file(sender, instance, **kwargs):
	instance.file.delete(False)
