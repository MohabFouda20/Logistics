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
    phone = models.CharField(max_length = 11 , null = False  , default = '123456789')
    pickupAddress = models.CharField(max_length = 200 , null=False , default ='enter pickup Address')
    wallet = models.IntegerField( null =False , default = 0)
    transferOption= models.CharField(max_length = 100 ,choices =choices , null = True , blank = False )
    # transferAccount= models.CharField()
    def __str__(self):
        return str(self.user)