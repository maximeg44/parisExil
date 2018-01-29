from django.http import HttpResponse
from django.template import loader
from .models import Personne, Jeune
from django.shortcuts import render, get_object_or_404
from webApplication.models import Accueillir
from django.db import connection
from collections import namedtuple
import datetime
from datetime import datetime
from test.datetimetester import DAY
from _datetime import timedelta

def index(request):
    #jeunes_fin_hebergement_list = Jeune.objects.all()
    #jeunes_fin_hebergement_list = {'nom': 'nom', 'prenom' :'prenom', 'dateFin' : 'dateFin', 'idPersonne': 'idPersonne'}
    #jeunes_fin_hebergement_list = namedtuple('J', 'nom, prenom, dateFin, id')
    #with connection.cursor() as cursor:
        #cursor.execute("SELECT nom, prenom, accueillir.dateFin, Personne.idPersonne FROM accueillir, Personne where Personne.idPersonne = accueillir.idPersonne")
        #jeunes_fin_hebergement_list = cursor.fetchall()
        #cursor.close()
    
    #jeunes_fin_hebergement_list = Accueillir.objects.all()
    start_date = datetime.today()
    delai = timedelta(7)
    end_date = start_date + delai
    #jeunes_fin_hebergement_list = Accueillir.objects.filter(datefin = [start_date,end_date])
    jeunes_fin_hebergement_list = Accueillir.objects.all().filter(datefin__lte=end_date) 
    
    
   # jeunes_fin_hebergement_list = row
    template = loader.get_template('webApplication/index.html')
    context = {
        'jeunes_fin_hebergement_list' : jeunes_fin_hebergement_list,
        }
    return HttpResponse(template.render(context, request))

def detailJeune(request, jeune_id):
    jeune = get_object_or_404(Personne, pk=jeune_id)
    return render(request, 'webApplication/detailJeune', {'jeune' : jeune})




