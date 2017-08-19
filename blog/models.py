from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=80, unique=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    title = models.CharField(max_length=100, null=True)
    text = models.TextField(null=True)

    def __str__(self):
        return format(self.title)