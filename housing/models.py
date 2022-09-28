from unittest.util import _MAX_LENGTH
from django.db import models


class Home(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name