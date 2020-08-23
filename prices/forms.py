from django import forms
from django.forms import ModelForm
from .models import OutstationPrice,Routes,Cab


def get_source():
    data = Routes.objects.all()
    return data


def get_destination():
    data = Routes.objects.values('destination')
    return data


def get_cabs():
    data = Cab.objects.values('model_name')
    return data


class OutstationPriceForm(ModelForm):
    class Meta:
        model = OutstationPrice
        fields = '__all__'
        source = get_source()
        destination = get_destination()
        cabs = get_cabs()

        widgets = {
            'source': forms.Select(choices=get_source(),attrs={'class': 'form-control'}),
        }
        widgets = {
            'destination': forms.Select(choices=get_destination(), attrs={'class': 'form-control'}),
        }
        widgets = {
            'cabs': forms.Select(choices=cabs, attrs={'class': 'form-control'}),
        }
