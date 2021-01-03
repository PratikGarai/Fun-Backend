from django.db import models

class Item(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.URLField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)