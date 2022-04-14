from unicodedata import name
from django.db import models

# Create your models here.


class SmartDeviceBrand(models.Model):
    ID=models.IntegerField(primary_key=True)
    name=models.TextField()
    createAt=models.DateField()
    def __str__(self):
        return self.name
class SmartDevice(models.Model):
    ID=models.IntegerField(primary_key=True)
    name=models.TextField()
    color=models.TextField()
    material=models.TextField()
    CPU=models.TextField()
    GPU=models.TextField()
    OS=models.TextField()
    screenSize=models.FloatField()
    storage=models.TextField()
    battery=models.TextField()
    weight=models.FloatField()
    warrantyPeriod=models.TextField()
    speaker=models.TextField()
    img=models.ImageField()
    smartDeviceBrand=models.ForeignKey(SmartDeviceBrand,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class MobilePhone(SmartDevice,models.Model):
    touchID=models.TextField()
    sims=models.TextField()
    frontCamera=models.TextField()
    rearCamera=models.TextField()
    def __str__(self):
        return self.name
class Laptop(SmartDevice, models.Model):
    type=models.TextField()
    webCam=models.TextField()
    keyborad=models.TextField()
    def __str__(self):
        return self.name
class SmartDeviceStats(models.Model):
    ID=models.IntegerField(primary_key=True)
    quantity=models.IntegerField()
    importPrice=models.FloatField()
    quantityLeft=models.IntegerField()
    createAt=models.DateField()
    smartDevice=models.ForeignKey(SmartDevice ,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.ID)
class SmartDeviceItem(models.Model):
    ID=models.IntegerField(primary_key=True)
    barcode=models.TextField()
    price=models.FloatField()
    discount=models.FloatField()
    smartDevice=models.OneToOneField(SmartDevice,on_delete=models.CASCADE)
    def __str__(self):
        return self.barcode