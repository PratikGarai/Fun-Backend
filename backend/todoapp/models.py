from django.db import models

priority_choices = [ (1,"High"),
                     (2,"Medium"),
                     (3,"Low") ]

class Todo(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    isComplete = models.BooleanField(default=False)
    priority = models.IntegerField(choices=priority_choices)
