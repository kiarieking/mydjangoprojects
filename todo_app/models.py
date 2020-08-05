from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Todo(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.pk

