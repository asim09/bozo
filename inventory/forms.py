from django import forms
from django.forms import ModelForm
from .models import Vendor,Cab,CabModels,Routes


def get_vendor_data():
    data = Vendor.objects.values('name')
    print(data)
    return data


class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'


class CabForm(ModelForm):
    class Meta:
        model = Cab
        fields = '__all__'
        vendor_name = get_vendor_data()
        widgets = {
            'age': forms.Select(choices=vendor_name,attrs={'class': 'form-control'}),
        }


class CabModelForm(ModelForm):
    class Meta:
        model = CabModels
        fields = '__all__'


class RouteForm(ModelForm):
    class Meta:
        model = Routes
        fields = '__all__'
