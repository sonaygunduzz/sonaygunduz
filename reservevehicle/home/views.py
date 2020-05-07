from  django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactFormu, ContactFormMessage

from vehicle.models import Vehicle

from vehicle.models import Category

from vehicle.models import Vehicle

from vehicle.models import Images


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Vehicle.objects.all()
    category = Category.objects.all()
    vehiclelist = Vehicle.objects.all()[:3]


    context={'setting' : setting,
             'category' : category,
             'page': 'home',
             'sliderdata': sliderdata,
             'vehiclelist': vehiclelist,
             }
    return render(request,'index.html',context)



def about(request):
    setting = Setting.objects.get(pk=1)
    context={'setting' : setting, 'page': 'about'}
    return render(request,'about.html',context)

def references(request):
    setting = Setting.objects.get(pk=1)
    context={'setting' : setting, 'page': 'references'}
    return render(request,'references.html',context)

def contact(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "your email sended successfully. Thank You ")
            return HttpResponseRedirect ('/contact')

    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context={'setting' : setting, 'form': form }
    return render(request,'contact.html',context)

def category_vehicles(request,id,slug):
    category = Category.objects.all()
    category_data = Category.objects.filter(parent_id=id)
    context = {'category': category,
               'category_data': category_data
               }
    return render(request, 'category_vehicles.html',context)

def vehicles(request, id, slug):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    category_data = Category.objects.get(pk=id)
    vehicles = Vehicle.objects.filter(category_id=id)
    context = {
            'category': category,
            'vehicles': vehicles,
            'category_data': category_data,
            'setting': setting
            }
    return render(request, 'vehicles.html', context)

def vehicle_detail(request, id, slug):
    category = Category.objects.all()
    vehicles = Vehicle.objects.get(id=id)
    images = Images.objects.filter(vehicle_id=id)
    context = {
            'category': category,
            'vehicles': vehicles,
            'images': images
            }
    return render(request, 'vehicle_detail.html', context)
