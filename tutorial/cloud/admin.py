# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from tutorial.cloud.models import General, Hosts , Costs


admin.site.register(General)
admin.site.register(Hosts)
admin.site.register(Costs)


# Register your models here.
