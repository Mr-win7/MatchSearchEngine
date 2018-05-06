# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    department = models.CharField(max_length=255, blank=True)
    url = models.URLField(max_length=2000, blank=True)
    time = models.DateField()

