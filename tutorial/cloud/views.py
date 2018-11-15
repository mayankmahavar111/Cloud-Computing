# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from tutorial.cloud.forms import GeneralForm
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


def General(request):


    if request.method=="POST":
        pass
    else:
        form = GeneralForm()
        return render(request,'general.html',{"form":form})