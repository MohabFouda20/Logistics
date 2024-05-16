from django.db import models
from User.models import AppUser 
from datetime import datetime


egypt_governorates = [
    ("Cairo", "Cairo"),
    ("Alexandria", "Alexandria"),
    ("Giza", "Giza"),
    ("Sharqia", "Sharqia"),
    ("Qalyubia", "Qalyubia"),
    ("Ismailia", "Ismailia"),
    ("Suez", "Suez"),
    ("Dakahlia", "Dakahlia"),
    ("Beheira", "Beheira"),
    ("Aswan", "Aswan"),
    ("Asyut", "Asyut"),
    ("Beni Suef", "Beni Suef"),
    ("Faiyum", "Faiyum"),
    ("Gharbia", "Gharbia"),
    ("Luxor", "Luxor"),
    ("Matrouh", "Matrouh"),
    ("Minya", "Minya"),
    ("Monufia", "Monufia"),
    ("New Valley", "New Valley"),
    ("North Sinai", "North Sinai"),
    ("Port Said", "Port Said"),
    ("Qena", "Qena"),
    ("Red Sea", "Red Sea"),
    ("Sohag", "Sohag"),
    ("South Sinai", "South Sinai"),
    ("Kafr El Sheikh", "Kafr El Sheikh"),
    ("Damietta", "Damietta")
    ]
class order(models.Model):
    shipper = models.ForeignKey (AppUser ,null = False , on_delete = models.CASCADE)
    name  = models.CharField(max_length = 100 , null = False , blank = False)
    phone = models.CharField(max_length = 50 , null = False , blank = False)
    government = models.CharField(max_length=100, choices=egypt_governorates , null = False , blank = False)
    address = models.CharField(max_length = 300 , null=False , blank= False)
    shipment_content = models.CharField(max_length = 100 , null = False , blank = False)
    shipment_weight = models.SmallIntegerField(null = False , blank = False , default= 1 )
    cash_on_delivery = models.IntegerField(null = False , blank = False , default = 0)
    shipping_price = models.IntegerField(null = False , blank = False , default = 0 , editable= False)
    net_income = models.IntegerField(null = False , blank = False  , default=0 , editable= False)
    order_status = models.CharField(
        max_length= 100 ,
        choices=[
        ('pending','pending'),
        ('ready for pickup','ready for pickup'),
        ('delivered','delivered'),
        ('canceled','canceled')
        ],
        default='ready for pickup',
        editable= False
        )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    def save(self,*args, **kwargs):
        shippingPriceList = {
        "Cairo": 50,
        "Alexandria": 60,
        "Giza": 50,
        "Sharqia": 60,
        "Qalyubia": 60,
        "Ismailia": 60,
        "Suez": 60,
        "Dakahlia": 60,
        "Beheira": 60,
        "Aswan": 70,
        "Asyut": 70,
        "Beni Suef": 60,
        "Faiyum": 60,
        "Gharbia": 60,
        "Luxor": 70,
        "Matrouh": 90,
        "Minya": 70,
        "Monufia": 60,
        "New Valley": 100,
        "North Sinai": 100,
        "Port Said": 70,
        "Qena": 70,
        "Red Sea": 100,
        "Sohag": 70,
        "South Sinai": 100,
        "Kafr El Sheikh": 60,
        "Damietta": 60
        }
        if self.government in shippingPriceList:
            self.shipping_price = shippingPriceList[self.government]
        self.net_income = self.cash_on_delivery - self.shipping_price  # try to calculate the net income in the model
        super().save(*args, **kwargs)
        

