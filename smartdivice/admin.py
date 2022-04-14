from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Laptop)
admin.site.register(models.MobilePhone)
admin.site.register(models.SmartDevice)
admin.site.register(models.SmartDeviceBrand)
admin.site.register(models.SmartDeviceItem)
admin.site.register(models.SmartDeviceStats)