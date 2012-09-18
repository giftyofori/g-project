from django.db import models
from django.contrib import admin

class Post(models.Model):
    name = models.CharField(max_length = 30)

    def __unicode__(self):
        return (self.name)
