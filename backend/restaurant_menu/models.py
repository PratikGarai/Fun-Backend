from django.db import models

class Item(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)


class  ItemImage(models.Model):

    url = models.URLField()
    item = models.ForeignKey(Item, related_name="images", on_delete=models.CASCADE)