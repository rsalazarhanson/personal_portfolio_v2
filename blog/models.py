from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField(max_length=250)
    date = models.DateField()
    body = models.TextField(max_length=2500)

    def __str__(self):
        return self.title
