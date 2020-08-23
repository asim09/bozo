from django import forms
from django.forms import ModelForm
from .models import Vendor,Cab,CabModels,Routes


def get_vendor_data():
    data = Vendor.objects.values('name')
    return data

def get_cab_models():
    data = CabModels.objects.values('model_name')
    return data


class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'


class CabForm(ModelForm):
    vendor_name = forms.Select(choices=get_vendor_data())
    class Meta:
        model = Cab
        fields = '__all__'
        exclude = ['cab_model','vendor']
        vendor_name = get_vendor_data()
        cab_models = get_cab_models()
        widgets = {
            'vendor': forms.Select(choices=vendor_name,attrs={'class': 'form-control'}),
        }


class CabModelForm(ModelForm):
    class Meta:
        model = CabModels
        fields = '__all__'


class RouteForm(ModelForm):
    class Meta:
        model = Routes
        fields = '__all__'
