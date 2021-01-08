from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    members = models.ManyToManyField(to="Member", related_name="meals")

class Member(models.Model):
    name  = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    address = models.TextField()

    def __str__(self, *args, **kwargs):
        return self.name