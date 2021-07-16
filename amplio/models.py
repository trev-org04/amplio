from django.db import models

class registration(models.Model):
    name = models.CharField(max_length=50)
    grade = models.CharField(max_length=10)
    date = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    extraInfo = models.TextField(max_length=1000)
