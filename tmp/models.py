from django.db import models


class Tmp(models.Model):
    name = models.CharField(max_length=63)
    description = models.TextField()
