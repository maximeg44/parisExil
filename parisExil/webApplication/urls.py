'''
Created on 27 janv. 2018

@author: Maxime
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('<int:jeune_id>/', views.detailJeune, name='detailJeune'),
    path('dispatch', views.dispatcher, name='dispatch'),
    path('listeHebergeurs/', views.listeHebergeurs, name='listeHebergeurs'),
    path('listeHebergeurs/<int:hebergeur_id>/', views.listeHebergeurs, name='listeHebergeurs'),
]