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


class WellInfo(models.Model):
        NumberOfEstablishedPlantsNearby = models.IntegerField()
        NumberOfDevelopmentalPlantsNearby = models.IntegerField()
        OperatorName = models.CharField(max_length=200)
        WellStatus = models.CharField(max_length=200)
        ConversionTechnology = models.CharField(max_length=200)
        CoolingType = models.CharField(max_length=200)
        AgeOfWellInYears = models.IntegerField() 
        WellDepthInMeters = models.IntegerField()
        
class GeoInfo(models.Model):
        Tempreature = models.IntegerField()
        ChemicalComposition = models.CharField(max_length=200)
        RockType = models.CharField(max_length=200)

class RiskProfile(models.Model):
        High = models.BooleanField()
        Medium = models.BooleanField()
        Low = models.BooleanField()
        Score = models.IntegerField()
        Notes = models.TextField()



