from django.http import HttpResponse
from django.template import loader
from .models import Personne, Jeune
from django.shortcuts import render, get_object_or_404

def index(request):
    jeunes_fin_hebergement_list = Personne.objects.all()
    template = loader.get_template('webApplication/index.html')
    context = {
        'jeunes_fin_hebergement_list' : jeunes_fin_hebergement_list,
        }
    return HttpResponse(template.render(context, request))

def detailJeune(request, jeune_id):
    jeune = get_object_or_404(Personne, pk=jeune_id)
    return render(request, 'webApplication/detailJeune', {'jeune' : jeune})