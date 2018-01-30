from django.http import HttpResponse
from django.template import loader
from .models import Personne, Jeune
from django.shortcuts import render, get_object_or_404
from webApplication.models import Accueillir, Parler
from datetime import datetime
from _datetime import timedelta

def index(request):
    start_date = datetime.today()
    delai = timedelta(7)
    end_date = start_date + delai
    jeunes_fin_hebergement_list = Accueillir.objects.all().filter(datefin__lte=end_date) 
    template = loader.get_template('webApplication/index.html')
    context = {
        'jeunes_fin_hebergement_list' : jeunes_fin_hebergement_list,
        }
    return HttpResponse(template.render(context, request))

def detailJeune(request, jeune_id):
    jeune = get_object_or_404(Jeune, pk=jeune_id)
    liste_langue_parler = Parler.objects.all().filter(idpersonne = jeune_id)
    template = loader.get_template('webApplication/detailJeune.html')
    context = {
        'jeune' : jeune, 
        'liste_langue_parler' : liste_langue_parler,
        }
    return HttpResponse(template.render(context, request))






