from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now()

    return render(
        request,
        "LetsDataCentreMonitoringApp/about.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'title' : "About LetsDataCentreMonitoringApp",
            'content' : "Example app page for Django."
        }
    )