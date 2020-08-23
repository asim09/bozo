from django.db import models
from inventory.models import Routes,Cab

# Create your models here.


class OutstationPrice(models.Model):
    route = models.ForeignKey(Routes,on_delete=models.SET_NULL,null=True)
    model_name = models.CharField(max_length=120)
    price = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.source
