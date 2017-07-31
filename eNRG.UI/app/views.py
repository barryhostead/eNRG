"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .forms import WellForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
            form = WellForm(request.POST)
            if form.is_valid():
                wellinstance = form.save(commit=False)
                wellinstance.Country = form.Meta.model.Country
                wellinstance.State = form.Meta.model.State
                wellinstance.City = form.Meta.model.City
                wellinstance.Well = form.Meta.model.Well

                wellinstance.save()

    else:
        form = WellForm()



    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'form': form
        }
    )

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
