from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.views import vehicles
from vehicle.models import Category

from vehicle.models import Vehicle


def index(request):
    return HttpResponse("Vehicle Page")
