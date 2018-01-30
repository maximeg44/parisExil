from django.http import HttpResponse
from django.template import loader
from .models import Personne
from django.shortcuts import render, get_object_or_404
from webApplication.models import Accueillir
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
    jeune = get_object_or_404(Personne, pk=jeune_id)
    return render(request, "webApplication/detailJeune.html", {'jeune' : jeune})

def listeHebergeurs(request, hebergeur_id = None):
    hebergeurs_list = Hebergeur.objects.all()
    template = loader.get_template('webApplication/listeHebergeurs.html')
    context={}
    context['hebergeurs_list'] = hebergeurs_list

    if hebergeur_id != None:
        hebergeurSelection = get_object_or_404(Hebergeur, idpersonne=hebergeur_id)
        context['hebergeurSelection'] = hebergeurSelection

    return HttpResponse(template.render(context, request))
