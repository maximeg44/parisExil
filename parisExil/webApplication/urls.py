'''
Created on 27 janv. 2018

@author: Maxime
'''
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:jeune_id>/', views.detailJeune, name='detailJeune'),
]