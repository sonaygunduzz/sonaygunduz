import json

from ckeditor_uploader.forms import SearchForm
from  django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactFormu, ContactFormMessage

from vehicle.models import Vehicle

from vehicle.models import Category

from vehicle.models import Vehicle

from vehicle.models import Images

from vehicle.models import Comment




def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Vehicle.objects.all()
    category = Category.objects.all()
    vehiclelist = Vehicle.objects.all()[:3]

    context={'setting' : setting,
             'category': category,
             'page': 'home',
             'sliderdata': sliderdata,
             'vehiclelist': vehiclelist,
             }
    return render(request,'index.html',context)



def about(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context={'setting' : setting, 'page': 'about', 'category' : category}
    return render(request,'about.html',context)

def references(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context={'setting' : setting, 'page': 'references', 'category': category}
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
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context={'setting' : setting, 'form': form, 'category': category  }
    return render(request,'contact.html',context)

def category_vehicles(request,id,slug):
    category = Category.objects.all()
    category_data = Category.objects.filter(parent_id=id)
    vehicles = Vehicle.objects.filter(category_id=id)
    context = {'vehicles':vehicles,
               'category': category,
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
    comments = Comment.objects.filter(vehicle_id=id, status='True')
    context = {
            'category': category,
            'vehicles': vehicles,
            'images': images,
            'comments': comments,
            }
    return render(request, 'vehicle_detail.html', context)

def vehicle_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['q']
            vehicles = Vehicle.objects.filter(title__icontains=query)
            context = {'vehicles': vehicles,
                       'category': category,

                       }
            return render(request, 'vehicles_search.html', context)
        return HttpResponseRedirect('/')

def vehicle_search_auto(request):

    if request.is_ajax():
        q = request.GET.get('term', '')
        vehicle = Vehicle.objects.filter(title__icontains=q)
        results = []
        for rs in vehicle:
            vehicle_json = {}
            vehicle_json = rs.title
            results.append(vehicle_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'

    return HttpResponse(data, mimetype)
