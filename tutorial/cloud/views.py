# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from tutorial.cloud.forms import GeneralForm,HostForm,CostForm
from django.shortcuts import render,redirect
from .models import  General as gen, Hosts as hos, Costs as cos
from django.views.generic import TemplateView
from django.db.models import Max


key=0
def General(request):
    global key
    if request.method=="POST":
        form = GeneralForm(request.POST)
        if form.is_valid():
            key=gen.objects.all().aggregate(Max('key'))
            if  key['key__max']== None :
                print key, key['key__max'], key['key__max'] == None
                key=1
            else:
                key=key['key__max']+1

            AllocationPolicy=form.cleaned_data['AllocationPolicy']
            os=form.cleaned_data['os']
            Hypervisor=form.cleaned_data['Hypervisor']
            SchedulingInterval=form.cleaned_data['SchedulingInterval']
            UpperThreshold=form.cleaned_data['UpperThreshold']
            LowerThreshold=form.cleaned_data['LowerThreshold']
            VMmigrations=form.cleaned_data['VMmigrations']
            MonitoringInterval=form.cleaned_data['MonitoringInterval']

            general = gen.objects.create(
                key=key,
                AllocationPolicy=AllocationPolicy,
                os=os,
                Hypervisor=Hypervisor,
                SchedulingInterval = SchedulingInterval,
                UpperThreshold = UpperThreshold,
                LowerThreshold=LowerThreshold,
                VMmigrations=VMmigrations,
                MonitoringInterval=MonitoringInterval,
            )
            general.save()

            return redirect('/Host/')
        else:
            return  redirect('/General/')
    else:
        form = GeneralForm()
        return render(request,'general.html',{"form":form})



def host(request):
    global key

    if request.method=="POST":
        form = HostForm(request.POST)
        if form.is_valid():
            amount=form.cleaned_data['amount']
            ram=form.cleaned_data['ram']
            Bandwidth=form.cleaned_data['Bandwidth']
            Storage=form.cleaned_data['Storage']
            MaxPower=form.cleaned_data['MaxPower']
            StaticPower=form.cleaned_data['StaticPower']
            ProcessingElement=form.cleaned_data['ProcessingElement']
            MPS=form.cleaned_data['MPS']
            HOST = hos.objects.create(
                key=key,
                amount=amount,
                ram = ram,
                Bandwidth = Bandwidth,
                Storage =Storage,
                MaxPower=MaxPower,
                StaticPower=StaticPower,
                ProcessingElement=ProcessingElement,
                MPS=MPS
            )
            HOST.save()
            return redirect('/Cost/')
        else:
            return redirect('/Hosts/')

    else:
        print key
        form = HostForm()
        return render(request,'general.html',{"form":form})


def cost(request):
    global key

    if request.method=="POST":
        form = CostForm(request.POST)
        if form.is_valid():
            ProcessingCost=form.cleaned_data['ProcessingCost']
            MemoryCost=form.cleaned_data['MemoryCost']
            StorageCost=form.cleaned_data['StorageCost']
            BandwidthCost=form.cleaned_data['BandwidthCost']
            COST = cos.objects.create(
                key=key,
                ProcessingCost=ProcessingCost,
                MemoryCost=MemoryCost,
                StorageCost=StorageCost,
                BandwidthCost=BandwidthCost
            )
            COST.save()
            return redirect('/ask/')
        else:
            return redirect('/Cost/')
    else:
        form = CostForm()
        return render(request,'general.html',{"form":form})

def ask(request):
    if request.method=='POST':
        pass
    else:
        return render(request,'ask.html')