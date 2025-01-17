from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
    path('reservations/', views.reservations, name='reservations'),
    path('reservationdetail/<int:id>', views.reservationdetail, name='reservationdetail'),
    path('mycomments/', views.comments, name='comments'),
    path('deletecomment/<int:id>', views.deletecomment, name='deletecomment'),
   ]