from django.db import models

# Create your models here.
class Blue(models.Model):
    count = models.IntegerField()
    time = models.FloatField()

class Red(models.Model):
    count = models.IntegerField()
    time = models.FloatField()
