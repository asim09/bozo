from django.shortcuts import render,redirect
from .forms import OutstationPriceForm

# Create your views here.


def cab_models_create(request):
    form = OutstationPriceForm()
    if request.method == 'POST':
        form = OutstationPriceForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('cab_models_view')
    context = {'form': form}

    return render(request, 'prices/create_price.html', context)
