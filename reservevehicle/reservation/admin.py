from django.contrib import admin

# Register your models here.
from reservation.models import ShopCart

from reservation.models import ReservationVehicle

from reservation.models import Reservation


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'vehicle', 'price', 'quantity', 'amount']
    list_filter = ['user']

class ReservationVehicleline(admin.TabularInline):
    model = ReservationVehicle
    readonly_fields = ('user', 'vehicle', 'price', 'quantity', 'amount')
    can_delete = False
    extra = 0

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'city', 'total', 'status']
    list_filter = ['status']
    readonly_fields = ('user', 'address', 'city', 'country', 'phone', 'first_name', 'last_name', 'ip', 'total')
    inlines = [ReservationVehicleline]


class ReservationVehicleAdmin(admin.ModelAdmin):
    list_display = ['user', 'vehicle', 'price', 'quantity', 'amount']
    list_filter = ['user']


admin.site.register( ShopCart, ShopCartAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(ReservationVehicle, ReservationVehicleAdmin)