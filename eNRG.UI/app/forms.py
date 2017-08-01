"""
Definition of forms.
"""

from django import forms
from app.models import WellInstance,  WellInfo, GeoInfo, RiskProfile


class WellForm(forms.ModelForm):

    class Meta:
        model = WellInstance
        fields = ['Country', 'State', 'City', 'Well']

class WellInfoForm(forms.ModelForm):

    class Meta:
        model = WellInfo
        fields = ['NumberOfEstablishedPlantsNearby','NumberOfDevelopmentalPlantsNearby','OperatorName', 'WellStatus', 'ConversionTechnology', 'CoolingType', 'AgeOfWellInYears','WellDepthInMeters']

class GeoInfoForm(forms.ModelForm):
    class Meta:
        model = GeoInfo
        fields = ['Tempreature','ChemicalComposition','RockType']

class RiskProfileForm(forms.ModelForm):
    class Meta:
        model = RiskProfile
        fields = ['High','Medium','Low','Score','Notes']