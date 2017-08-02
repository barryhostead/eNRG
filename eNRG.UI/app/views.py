"""
Definition of views.
"""
from django.views.generic import TemplateView, FormView
from django.shortcuts import render
from django.http import HttpRequest,HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from .forms import WellForm, WellInfoForm, GeoInfoForm, RiskProfileForm
#from django.contrib import messages
#import folium
#import google
import GeoLocationData as gl

class home(TemplateView):
    template_name = 'app/index.html'

    def get(self, request, *args, **kwargs):
        """Renders the home page."""
        wellform = WellForm(self.request.GET or None)
        wellinfoform = WellInfoForm(self.request.GET or None)
        geoinfoform = GeoInfoForm(self.request.GET or None)
        riskprofileform = RiskProfileForm(self.request.GET or None)

        title= 'eNRG'
        year = datetime.now().year

        context = self.get_context_data(**kwargs)
        context['wellform'] = wellform
        context['wellinfoform'] = wellinfoform
        context['geoinfoform'] = geoinfoform
        context['riskprofileform'] = riskprofileform
        context['title'] = title
        context['year'] = year

        return self.render_to_response(context)
    

    

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

class WellFormView(FormView):
    form_class = WellForm
    template_name = 'app/index.html'
    success_url = '/'    

    def post(self, request, *args, **kwargs):
        wellform = self.form_class(request.POST)
        wellinfoform = WellInfoForm()
        geoinfoform = GeoInfoForm()
        riskprofileform = RiskProfileForm()
        
        if wellform.is_valid():
            wellform.save()
            
            getinfo(request, request.POST['Well'])

            return self.render_to_response(
                self.get_context_data(
                    success=True
                    )
                )
        else:
            return self.render_to_response(
                self.get_context_data(
                    wellform=wellform,
                    wellinfoform=wellinfoform,
                    geoinfoform=geoinfoform,
                    riskprofileform=riskprofileform

                    )
                )

                

class WellInfoFormView(FormView):
    form_class = WellInfoForm
    template_name = 'app/index.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        wellform = WellForm()
        wellinfoform = self.form_class(request.POST)
        geoinfoform = GeoInfoForm()
        riskprofileform = RiskProfileForm()
        
        if wellinfoform.is_valid():
            wellinfoform.save()
            return self.render_to_response(
                self.get_context_data(
                    success=True
                    )
                )
        else:
            return self.render_to_response(
                self.get_context_data(
                    wellform=wellform,
                    wellinfoform=wellinfoform,
                    geoinfoform=geoinfoform,
                    riskprofileform =riskprofileform

                    )
                )

        
class GeoInfoFormView(FormView):
    form_class = GeoInfoForm
    template_name = 'app/index.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        wellform = WellForm()
        wellinfoform = WellInfoForm()
        geoinfoform = self.form_class(request.POST)
        riskprofileform = RiskProfileForm()
        
        if geoinfoform.is_valid():
            geoinfoform.save()
            return self.render_to_response(
                self.get_context_data(
                    success=True
                    )
                )
        else:
            return self.render_to_response(
                self.get_context_data(
                    wellform=wellform,
                    wellinfoform=wellinfoform,
                    geoinfoform=geoinfoform,
                    riskprofileform =riskprofileform

                    )
                )

class RiskProfileFormView(FormView):
    form_class = RiskProfileForm
    template_name = 'app/index.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        wellform = WellForm()
        wellinfoform = WellInfoForm()
        geoinfoform = GeoInfoForm()
        riskprofileform = self.form_class(request.POST)
        
        if riskprofileform.is_valid():
            riskprofileform.save()
            return self.render_to_response(
                self.get_context_data(
                    success=True
                    )
                )
        else:
            return self.render_to_response(
                self.get_context_data(
                    wellform=wellform,
                    wellinfoform=wellinfoform,
                    geoinfoform=geoinfoform,
                    riskprofileform =riskprofileform

                    )
                )


def getinfo(request, wellname):
    wells=gl.GetWells()

    for well in wells:
        if well.Well == wellname:
            selectedwell=well

            gl.CreateMap(selectedwell[6],selectedwell[5])
    
    return HttpResponseRedirect('/')
