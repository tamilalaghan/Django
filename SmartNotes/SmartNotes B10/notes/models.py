from django.db import models

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created = models.TimeField(auto_now_add=True)
