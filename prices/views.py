from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import OutstationPriceForm
from inventory.models import Routes,Vendor
from .models import OutstationPrice

# Create your views here.


def outstation_price(request):
    data = Routes.objects.all()
    vendors = Vendor.objects.all()
    context = {
        'data': data,
        'vendors': vendors,
    }
    if request.method == 'POST':
        s = request.POST.get('source')
        d = request.POST.get('destination')
        v = request.POST.get('vendor_name')
        p = request.POST.get('price')
        data = Routes.objects.get(source=s,destination=d)
        data = OutstationPrice(route_id=data.id,model_name=v,price=p)
        data.save()
        # return redirect('')

    return render(request, 'prices/create_price.html', context)




# def cab_models_create(request):
#     form = OutstationPriceForm()
#     if request.method == 'POST':
#         form = OutstationPriceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # return redirect('cab_models_view')
#     context = {'form': form}
#
#     return render(request, 'prices/create_price.html', context)
