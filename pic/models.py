# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db import models

# Create your models here.
class UploadFile(models.Model):
    file1 = models.FileField(upload_to="")
    file2 = models.FileField(upload_to="")

@receiver(post_delete, sender=UploadFile)
def delete_file(sender, instance, **kwargs):
    instance.file.delete(False)