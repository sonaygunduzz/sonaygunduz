from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.utils.crypto import get_random_string
from vehicle.models import Category

from reservation.models import ShopCart

from reservation.models import ShopCartForm

from reservation.models import ReservationForm

from reservation.models import Reservation

from reservation.models import ReservationVehicle

from vehicle.models import Vehicle

from home.models import UserProfile


def index(request):
    return HttpResponse("Reservation App ")

@login_required(login_url='/login')
def addtocart(request,id):
    url = request.META.get('HTTP_REFERER')

    current_user = request.user
    checkvehicle = ShopCart.objects.filter(vehicle_id =id)
    if checkvehicle:
        control = 1
    else:
        control = 0

    if request.method == 'POST':

        form = ShopCartForm(request.POST)
        if form.is_valid():
                data = ShopCart()
                data.user_id = current_user.id
                data.quantity = form.cleaned_data['quantity']
                data.vehicle_id = id
                data.save()
        request.session['cart_items'] = ShopCart.objects.filter(user_id =current_user.id).count()
        messages.success(request, " Araç Başarı ile Sepete eklendi! ")
        return HttpResponseRedirect(url)

    else:
        if control == 1:
            data = ShopCart()
            data.quantity += 1
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.vehicle_id = id
            data.quantity = 1
            data.save()
        request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
        messages.success(request, " Araç Başarı ile Sepete eklendi! ")
        return HttpResponseRedirect(url)

    messages.warning(request, "Araç sepete eklenemedi")
    return HttpResponseRedirect(url)


@login_required(login_url='/login')
def shopcart(request):
    category = Category.objects.all()
    current_user = request.user
    schopcart = ShopCart.objects.filter(user_id = current_user.id)
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()

    total =0
    for rs in schopcart:
      total += rs.vehicle.price * rs.quantity

    context = {
                'schopcart': schopcart,
                'category': category,
                'total': total,
            }
    return render(request, 'Shopcart_vehicles.html', context)

@login_required(login_url='/login')
def deletefromcart(request,id):
    ShopCart.objects.filter(id=id).delete()
    current_user = request.user
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
    messages.success(request, "Ürün sepetten başarı ile silindi")
    return HttpResponseRedirect("/shopcart")

@login_required(login_url='/login')
def reservationvehicle(request):
    category = Category.objects.all()
    current_user = request.user
    schopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in schopcart:
        total += rs.vehicle.price * rs.quantity

    if request.method == 'POST':
        form = ReservationForm(request.POST)

        if form.is_valid():
            data = Reservation()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            reservationcode =get_random_string(5).upper()
            data.code = reservationcode
            data.save()

            schopcart = ShopCart.objects.filter(user_id = current_user.id)
            for rs in schopcart:
                detail = ReservationVehicle()
                detail.reservation_id = data.id
                detail.vehicle_id = rs.vehicle_id
                detail.user_id = current_user.id
                detail.quantity = rs.quantity

                vehicle = Vehicle.objects.get(id=rs.vehicle_id)
                vehicle.amount -= rs.quantity
                vehicle.save()

                detail.price = rs.vehicle.price
                detail.amount = rs.amount
                detail.save()

            ShopCart.objects.filter(user_id= current_user.id).delete()
            request.session['cart_items']=0
            messages.success(request,"Your Reservation has been completed!")
            return render(request, 'Reservation_Completed.html', {'reservationcode': reservationcode, 'category': category})
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect("/reservation/reservationvehicle")

    form = ReservationForm()
    profile = UserProfile.objects.get(user_id = current_user.id)
    context = {
                'schopcart': schopcart,
                'category': category,
                'total': total,
                'form': form,
                'profile': profile,
             }
    return render(request, 'Reservation_Form.html', context)
