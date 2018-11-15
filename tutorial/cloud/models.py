# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class General(models.Model):
    key = models.IntegerField()
    AllocationPolicy = models.CharField(max_length=100, default='')
    os =models.CharField(max_length=100 , default='')
    Hypervisor = models.CharField(max_length=100 , default= '')
    SchedulingInterval = models.CharField(max_length=100 , default= ' ')
    UpperThreshold  = models.FloatField()
    LowerThreshold = models.FloatField()
    VMmigrations = models.CharField(max_length=100 , default=' ')
    MonitoringInterval = models.IntegerField()
    class Meta:
        ordering = ('key',)

class Hosts(models.Model):
    key = models.ForeignKey(General,on_delete=models.CASCADE)
    amount = models.IntegerField()
    ram = models.FloatField()
    Bandwidth = models.FloatField()
    Storage = models.FloatField()
    MaxPower = models.IntegerField()
    StaticPower = models.IntegerField()
    ProcessingElement = models.IntegerField()
    MPS= models.CharField(max_length=100 , default=' ')

    class Meta:
        ordering = ('key' ,)

class Costs(models.Model) :
    key =models.ForeignKey(General,on_delete=models.CASCADE)
    ProcessingCost =  models.FloatField()
    MemoryCost =models.FloatField()
    StorageCost  = models.FloatField()
    BandwidthCost = models.FloatField()


    class Meta :
        ordering=('key' ,)

