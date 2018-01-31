from django.http import HttpResponse
from django.template import loader
from .models import Personne, Jeune
from django.shortcuts import render, get_object_or_404
from webApplication.models import Accueillir, Parler
from datetime import datetime
from _datetime import timedelta
from .models import Hebergeur

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

def dispatcher(request):
    template = loader.get_template('webApplication/dispatch.html')
    context = {
        
        }
    return HttpResponse(template.render(context,request))



def listeHebergeurs(request, hebergeur_id = None):
    hebergeurs_list = Hebergeur.objects.all()
    template = loader.get_template('webApplication/listeHebergeurs.html')
    context={}
    context['hebergeurs_list'] = hebergeurs_list

    if hebergeur_id != None:
        hebergeurSelection = get_object_or_404(Hebergeur, idpersonne=hebergeur_id)
        context['hebergeurSelection'] = hebergeurSelection

    return HttpResponse(template.render(context, request))

def listeJeunes(request, jeune_id = None):
    jeunes_list = Jeune.objects.all()
    jeunes_heberges_list = Accueillir.objects.values_list('idpersonne',flat=True)
    template = loader.get_template('webApplication/listeJeunes.html')
    context={}
    context['jeunes_list'] = jeunes_list
    context['jeunes_heberges_list'] = jeunes_heberges_list

    if jeune_id != None:
        jeuneSelection = get_object_or_404(Jeune, idpersonne=jeune_id)
        context['jeuneSelection'] = jeuneSelection

    return HttpResponse(template.render(context, request))