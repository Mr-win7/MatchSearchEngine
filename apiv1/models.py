# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from hanziconv import HanziConv

from django.db import models

# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    department = models.CharField(max_length=255, blank=True)
    url = models.FileField()
    time = models.DateField()

    def save(self, *args, **kwargs):
        self.content = HanziConv.toSimplified(self.content)
        self.title = HanziConv.toSimplified(self.title)
        super(Document, self).save(*args, **kwargs)

