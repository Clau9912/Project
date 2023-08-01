from django.db import models
from django.conf import settings


# Create your models here.
class Upload(models.Model) :
    name = models.CharField(max_length=50)
    mfile = models.CharField(max_length=100)
    category = models.BooleanField()

    def __str__(self) :
        return self.name
