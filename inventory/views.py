from django.shortcuts import render, redirect
from .models import CabModels, Vendor,Cab
from .forms import CabModelForm, VendorForm,CabForm,RouteForm
# from users.views import *
from django.contrib.auth.decorators import login_required


# Create your views here.


## Create Cab Inventory:
@login_required(login_url='user_login')
def cab_view(request):
    cabs = Cab.objects.all()
    context = {'cabs': cabs}
    return render(request, 'inventory/cab/cab_view.html', context)

@login_required(login_url='user_login')
def cab_create(request):
    form = CabForm()
    if request.method == 'POST':
        form = CabForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            # return redirect('cab_view')
    context = {'form': form}

    return render(request, 'inventory/cab/create_cab.html', context)

@login_required(login_url='user_login')
def cab_update(request,id):
    cab = Cab.objects.get(id=id)
    form = CabForm(instance=cab)
    if request.method == 'POST':
        form = CabForm(request.POST,instance=cab)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('cab_view')
    context = {'form': form}
    return render(request, 'inventory/cab/create_cab.html', context)




## Vendor Create
@login_required(login_url='user_login')
def vendor_view(request):
    vendors = Vendor.objects.all()
    context = {'vendors': vendors}
    return render(request, 'inventory/vendor/vendor_view.html', context)


@login_required(login_url='user_login')
def vendor_create(request):
    form = VendorForm()
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor_view')
    context = {'form': form}

    return render(request, 'inventory/vendor/create_vendor.html', context)



## Cab Model Create
@login_required(login_url='user_login')
def cab_models_view(request):
    cab_models = CabModels.objects.all()
    context = {'cab_models': cab_models}
    return render(request, 'inventory/cab_model/cab_model_view.html', context)

@login_required(login_url='user_login')
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
# def cab_view(request):
#     cabs = Cab.objects.all()
#     context = {'cabs': cabs}
#     return render(request, 'inventory/cab/cab_view.html', context)

@login_required(login_url='user_login')
def route_create(request):
    form = RouteForm()
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('cab_view')
    context = {'form': form}

    return render(request, 'inventory/route/create_route.html', context)
