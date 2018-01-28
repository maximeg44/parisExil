from django.http import HttpResponse
from django.template import loader
from .models import Personne, Jeune
from django.shortcuts import render, get_object_or_404
from webApplication.models import Accueillir
from django.db import connection

def index(request):
    #jeunes_fin_hebergement_list = Jeune.objects.all()
    with connection.cursor() as cursor:
        cursor.execute("SELECT nom, prenom, accueillir.dateFin, Personne.idPersonne FROM accueillir, Personne where Personne.idPersonne = accueillir.idPersonne")
        row = cursor.fetchall()
    jeunes_fin_hebergement_list = row[0]
    template = loader.get_template('webApplication/index.html')
    context = {
        'jeunes_fin_hebergement_list' : jeunes_fin_hebergement_list,
        }
    return HttpResponse(template.render(context, request))

def detailJeune(request, jeune_id):
    jeune = get_object_or_404(Personne, pk=jeune_id)
    return render(request, 'webApplication/detailJeune', {'jeune' : jeune})