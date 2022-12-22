from django.db import models

class Question(models.Model):
    original_url = models.CharField(max_length=256)
    hash = models.CharField(max_length=10)
    creatin_date = models.DateTimeField('creation date')
