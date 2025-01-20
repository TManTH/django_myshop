from django.db import models

class Country(models.Model):
    country = models.CharField(max_length=50)
    def __str__(self):
        return self.country

class Product(models.Model):
    name = models.CharField(max_length=100)
    #category = models.
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=500)
    #specifications = models.
    def __str__(self):
        return self.name

