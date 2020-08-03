from django.db import models
from inventory.models import Routes,Cab

# Create your models here.

class Outstation_Price(models.Model):
    source = models.ForeignKey(Routes,on_delete=models.SET_NULL,null=True)
    destination = models.ForeignKey(Routes,on_delete=models.SET_NULL,null=True)
    model_name = models.ForeignKey(Cab,on_delete=models.SET_NULL,null=True)
    price = models.IntegerField()


    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name
