from django.db import models

# Create your models here.
class model(models.Model):
    vm = models.IntegerField()
    view = models.IntegerField()
    information = models.CharField(max_length=5)