from django import forms
from django.forms import ModelForm
from .models import Outstation_Price,Routes,Cab


def get_source():
    data = Routes.objects.values('source')
    return data

def get_destination():
    data = Routes.objects.values('destination')
    return data

def get_cabs():
    data = Cab.objects.values('model_name')
    return data


class OutstationPriceForm(ModelForm):
    class Meta:
        model = Outstation_Price
        fields = '__all__'
        source = get_source()
        destination = get_destination()
        cabs = get_cabs()
        widgets = {
            'source': forms.Select(choices=get_source,attrs={'class': 'form-control'}),
            'destination': forms.Select(choices=get_destination, attrs={'class': 'form-control'}),
            'cabs': forms.Select(choices=get_cabs, attrs={'class': 'form-control'}),
        }
