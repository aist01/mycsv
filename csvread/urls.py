from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('open', views.open_csv, name='open'),
]

