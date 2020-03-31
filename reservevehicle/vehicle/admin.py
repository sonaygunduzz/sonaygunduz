from django.contrib import admin



# Register your models here.
from vehicle.models import Category

from vehicle.models import Vehicle

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', ]
    list_filter = ['status']

class VehicleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'amount', 'image', 'status', ]
    list_filter = ['status', 'category']

admin.site.register(Category, CategoryAdmin)

admin.site.register(Vehicle, VehicleAdmin)
