from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=20)
    published = models.DateTimeField()
    content = models.TextField()
