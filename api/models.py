from django.db import models

# Create your models here.
class Flight(models.Model):
    id = models.AutoField(primary_key=True)
    placeIcon = models.ImageField(upload_to='destination_images')
    origin = models.CharField(max_length = 50)
    destination = models.CharField(max_length = 50)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    price = models.IntegerField(default = 0)
