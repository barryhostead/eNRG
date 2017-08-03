"""
Definition of urls for eNRGUI.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.views.generic import TemplateView
import app.forms
from app.views import home, WellFormView, WellInfoFormView, GeoInfoFormView, RiskProfileFormView


# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home.as_view(), name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^DecisionTree', app.views.about, name='DecisionTree'),
    url(r'^search/$', app.views.WellFormView.as_view(), name='Search'),
    url(r'^wellinfo/$', app.views.WellInfoFormView.as_view(), name='WellInfo'),
    url(r'^geoinfo/$', app.views.GeoInfoFormView.as_view(), name='GeoInfo'),
    url(r'^riskprofile/$', app.views.RiskProfileFormView.as_view(), name='RiskProfile'),
    url(r'^getinfo/(\d+)/$', app.views.getinfo, name='getinfo')    ,
   

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     #url(r'^admin/', include(admin.site.urls)),
]
