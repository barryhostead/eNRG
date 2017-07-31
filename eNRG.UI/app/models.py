"""
Definition of models.
"""
from django.db import models

# Create your models here.
class WellInstance(models.Model):

    CountryChoices    = (('US','United States of America'),('UK','United Kingdon'))
    StateChoices    = (('US','United States of America'),('UK','United Kingdon'))
    CityChoices    = (('US','United States of America'),('UK','United Kingdon'))
    WellChoices    = (('US','United States of America'),('UK','United Kingdon'))


    Country = models.CharField(max_length=200, choices = CountryChoices, )
    State = models.CharField(max_length=200 , choices = StateChoices, )
    City = models.CharField(max_length=200, choices = CityChoices, )
    Well = models.CharField(max_length=200, choices = WellChoices, )

    def __str__(self):
        return self.Well