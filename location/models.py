from django.db import models

class Library(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Rack(models.Model):
    number = models.IntegerField()
    location_iddentifier = models.CharField(max_length=50)
    
    def __str__(self):
            return f"{self.number} | {self.location_iddentifier}"