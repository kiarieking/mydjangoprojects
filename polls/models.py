from django.db import models


class Tasks(models.Model):
    added_date = models.DateTimeField()
    task = models.CharField(max_length=700)
