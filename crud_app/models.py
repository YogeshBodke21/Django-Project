from django.db import models

# Create your models here.
class Laptop(models.Model):
    laptop_id = models.IntegerField(unique=True)
    model_name = models.CharField(max_length=70)
    brand = models.CharField(max_length=70)
    ram = models.IntegerField()
    processor = models.CharField(max_length=20)
    price = models.FloatField()
