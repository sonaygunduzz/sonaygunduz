from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.views import vehicles
from vehicle.models import Category

from vehicle.models import Vehicle

from vehicle.models import CommentForm

from vehicle.models import Comment


def index(request):
    return HttpResponse("Vehicle Page")

def addcomment(request,id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form =CommentForm(request.POST)
        if form.is_valid():
            current_user = request.user
            data = Comment()
            data.user_id= current_user.id
            data.vehicle_id = id
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "yorumunuz başarılı bir şekilde gönderildi")

            return HttpResponseRedirect(url)

    messages.warning(request, "yorumunuz kaydedilemedi. Lütfen kontrol ediniz ")

    return HttpResponseRedirect(url)
