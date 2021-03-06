from django.db import models
# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    mobile = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name



class CabModels(models.Model):
    model_name = models.CharField(max_length=120)
    image = models.ImageField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.model_name

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Cab(models.Model):
    model_name = models.CharField(max_length=120)
    seats = models.IntegerField()
    city = models.CharField(max_length=120)
    cab_model = models.ForeignKey(CabModels,on_delete=models.SET_NULL,null=True)

    vendor = models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.model_name


#Routes

class Routes(models.Model):
    TRIP = (
        ('outstation','outstation'),
    )
    source = models.CharField(max_length=120)
    destination = models.CharField(max_length=120)
    trip_type = models.CharField(max_length=120,choices=TRIP)
    distance = models.IntegerField()
    travel_time = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    # def __str__(self):
    #     return self.source
