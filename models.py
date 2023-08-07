from django.db import models
class restaurant(models.Model):
    name = models.CharField(max_length=30)
    Address = models.CharField(max_length=100)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    def __str__(self):
        return self.name

# Create your models here.
