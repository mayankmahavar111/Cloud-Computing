
from django.conf.urls import url , include
from tutorial.cloud import views

urlpatterns = [
    url('General/$', views.General),

]