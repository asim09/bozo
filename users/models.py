from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120,null=True)
    mobile = models.IntegerField(null=True)
    soft_delete = models.BooleanField(default=False,null=True)

    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name
