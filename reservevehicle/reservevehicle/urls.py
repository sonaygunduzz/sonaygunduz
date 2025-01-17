"""reservevehicle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home import views
from vehicle import views as vehicleviews
from reservation import views as reservationviews

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', include('home.urls')),
    path('vehicle/', include('vehicle.urls')),
    path('reservation/', include('reservation.urls')),
    path('user/',include('user.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('about/', views.about, name = 'about'),
    path('references/', views.references, name='references'),
    path('contact/', views.contact, name='contact'),
    path('category/<int:id>/<slug:slug>/', views.vehicles, name='vehicles'),
    path('categories/<int:id>/<slug:slug>/', views.category_vehicles, name='category_vehicles'),
    path('vehicle/<int:id>/<slug:slug>/', views.vehicle_detail, name='vehicle_detail'),
    path('search/', views.vehicle_search, name='vehicle_search'),
    path('search_auto/', views.vehicle_search_auto, name='vehicle_search_auto'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('shopcart/', reservationviews.shopcart, name='shopcart'),
    path('faq/', views.faq, name='faq'),

]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
