from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.mainsite_index, name="index"),
]