'''
Created on 27 janv. 2018

@author: Maxime
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.connexion, name='connexion'),
    path('index/', views.index, name='index'),
    path('dispatch', views.dispatcher, name='dispatch'),
    path('listeHebergeurs/', views.listeHebergeurs, name='listeHebergeurs'),
    path('listeHebergeurs/<int:hebergeur_id>/', views.listeHebergeurs, name='listeHebergeurs'),
    path('listeHebergeurs/delete/<int:pk>/', views.deleteHebergeur, name='deleteHebergeur'),
    path('listeJeunes/', views.listeJeunes, name='listeJeunes'),
    path('listeJeunes/<int:jeune_id>/', views.listeJeunes, name='listeJeunes'),
    path('listeJeunes/delete/<int:pk>/', views.deleteJeune, name='deleteJeune'),
]