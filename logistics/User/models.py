from django.db import models
from django.contrib.auth.models import User
# Create your models here.
choices = {
    ('bank Transfer','bank Transfer'),
    ('smart wallet','smart wallet'),
           }
class user (models.Model):
    user =models.OneToOneField(User ,null = True , on_delete = models.CASCADE) 
    # ID = models.AutoField(editable=False)
    phone = models.CharField(max_length = 11 , null = False , blank = False)
    pickupAddress = models.CharField(max_length = 200 , null=False , blank= False)
    wallet = models.IntegerField( null =False , default = 0)
    transferOption= models.CharField(max_length = 100 ,choices =choices , null = True , blank = False )
    # transferAccount= models.CharField()
    def __str__(self):
        return str(self.user)
    
class PickupRequest(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    number_of_orders = models.IntegerField(null=True , blank=True)
    status = models.BooleanField(default=False)