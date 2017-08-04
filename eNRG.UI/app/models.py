"""
Definition of models.
"""
from django.db import models


# Create your models here.
class WellInstance(models.Model):

    CountryChoices    = (('US','United States of America'),('IN', 'Indonesia'))
    StateChoices    = (('CA','California'),('NY','New York'))
    CityChoices    = (('CA','California'),('LA','Lassen'))
    WellChoices    = (('S3','Sinclair 3'),('KH','Kellog Hot Spring'))


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
        Ph = models.CharField(max_length=200)
        CO2 = models.CharField(max_length=200)

class RiskProfile(models.Model):
        High = models.BooleanField()
        Medium = models.BooleanField()
        Low = models.BooleanField()
        Score = models.IntegerField()
        Notes = models.TextField()



