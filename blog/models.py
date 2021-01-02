from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField(max_length=250)
    body = models.TextField(max_length=2500)
