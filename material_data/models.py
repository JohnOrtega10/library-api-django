from django.db import models

class Editorial(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name
