from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CabModels, Vendor,Cab
from .forms import CabModelForm, VendorForm,CabForm,RouteForm
# from users.views import *
from django.contrib.auth.decorators import login_required
from users.decorators import *

# Create Cab Inventory:

@login_required(login_url='user_login')
@allowed_users(allowed_roles=['admin'])
def cab_view(request):
    cabs = Cab.objects.all()
    context = {'cabs': cabs}
    return render(request, 'inventory/cab/cab_view.html', context)


@login_required(login_url='user_login')
@allowed_users(allowed_roles=['admin'])
def cab_create(request):
    vendor = Vendor.objects.values('name','id')
    cab_model = CabModels.objects.values('model_name')
    context = {
        'vendor':vendor,
        'cab_model':cab_model}

    if request.method == 'POST':
        print(request.POST)
        model = request.POST.get('model')
        city = request.POST.get('city')
        vendor_id = request.POST.get('vendor')
        seats = request.POST.get('seats')
        vendor = Vendor.objects.get(id=vendor_id)
        cab_id = CabModels.objects.get(model_name=model)
        cab = Cab(model_name=model,seats=seats,city=city,vendor=vendor,cab_model=cab_id)
        cab.save()


    return render(request, 'inventory/cab/create_cab.html', context)


@login_required(login_url='user_login')
@allowed_users(allowed_roles=['admin'])
def cab_update(request,id):
    cab = Cab.objects.get(id=id)
    print('-----------')
    print(cab)
    print('-----------')
    context = {
        'cab':cab,
    }
    print()
    # vendor = Vendor.objects.get(id=)
    # cab_model = CabModels.objects.values('model_name')
    # context = {
    #     'vendor':vendor,
    #     'cab_model':cab_model}
    #
    # if request.method == 'POST':
    #     print(request.POST)
    #     model = request.POST.get('model')
    #     city = request.POST.get('city')
    #     vendor_id = request.POST.get('vendor')
    #     seats = request.POST.get('seats')
    #     vendor = Vendor.objects.get(id=vendor_id)
    #     cab_id = CabModels.objects.get(model_name=model)
    #     cab = Cab(model_name=model,seats=seats,city=city,vendor=vendor,cab_model=cab_id)
    #     cab.save()
    # cab = Cab.objects.get(id=id)
    # form = CabForm(instance=cab)
    # if request.method == 'POST':
    #     form = CabForm(request.POST,instance=cab)
    #     print(form)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('cab_view')
    # context = {'form': form}
    return render(request, 'inventory/cab/create_cab.html', context)


# Vendor Create


@login_required(login_url='user_login')
@allowed_users(allowed_roles=['admin'])
def vendor_view(request):
    vendors = Vendor.objects.all()
    context = {'vendors': vendors}
    return render(request, 'inventory/vendor/vendor_view.html', context)


@login_required(login_url='user_login')
@allowed_users(allowed_roles=['admin'])
def vendor_create(request):
    form = VendorForm()
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor_view')
    context = {'form': form}

    return render(request, 'inventory/vendor/create_vendor.html', context)


# Cab Model Create

@login_required(login_url='user_login')
@allowed_users(allowed_roles=['admin'])
def cab_models_view(request):
    cab_models = CabModels.objects.all()
    context = {'cab_models': cab_models}
    return render(request, 'inventory/cab_model/cab_model_view.html', context)


@login_required(login_url='user_login')
@allowed_users(allowed_roles=['admin'])
def cab_models_create(request):
    form = CabModelForm()
    if request.method == 'POST':
        form = CabModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cab_models_view')
    context = {'form': form}

    return render(request, 'inventory/cab_model/create_cab_model.html', context)


## Routes

# @login_required(login_url='user_login')
# @allowed_users(allowed_roles=['admin'])
# def cab_view(request):
#     cabs = Cab.objects.all()
#     context = {'cabs': cabs}
#     return render(request, 'inventory/cab/cab_view.html', context)

@login_required(login_url='user_login')
@allowed_users(allowed_roles=['admin'])
def route_create(request):
    form = RouteForm()
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('cab_view')
    context = {'form': form}

    return render(request, 'inventory/route/create_route.html', context)
