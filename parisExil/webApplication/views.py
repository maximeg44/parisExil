from django.http import HttpResponse
from django.template import loader
from .models import Personne, Jeune, Accueillir, Parler, Membre, Hebergeur
from django.shortcuts import render, get_object_or_404, redirect
from webApplication.models import Accueillir, Parler
from datetime import datetime
from _datetime import timedelta
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponseRedirect
from gc import get_objects
from django.contrib.auth.decorators import login_required
from django.conf.global_settings import DATETIME_FORMAT



# Méthode associé à la page d'accueil du site
# Elle permet de récupérer un ensemble de jeune n'était plus hébergé dans les 7 jours à venir.. 
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
    liste_langue_parler = Parler.objects.all().filter(idpersonne=jeune_id)
    template = loader.get_template('webApplication/detailJeune.html')
    context = {
        'jeune' : jeune,
        'liste_langue_parler' : liste_langue_parler,
        }
    return HttpResponse(template.render(context, request))

# Méthode associée à la page de dispatch
# Elle permet de récupérer la liste des hébergeurs et des jeunes afin de mettre en place le dispatch
@login_required
def dispatcher(request):
    if request.method == 'POST':
        accueillir = Accueillir()
        hebergeur = Hebergeur.objects.get(idpersonne=request.POST["selectHebergeur"])
        jeune = Jeune()

        
        
        hebergeur = Hebergeur.objects.get(idpersonne=request.POST["selectHebergeur"])
        jeune.idpersonne = Personne(request.POST["selectJeune"])
        hebergeur.idpersonne = Personne(request.POST["selectHebergeur"])
        
        
        """ RESTE A CONVERTIR LES PUTAINS DE DATE DE DD/MM/YY à YYYY-MM-DD"""
        accueillir.datedebut = request.POST["dateDebut"]
        accueillir.datefin = request.POST["dateFin"]
        accueillir.idpersonne = jeune.get_idpersonne()
        accueillir.idpersonne_1 = hebergeur.get_idpersonne()        
        accueillir.idpersonne_2 = Personne(request.user.id)        
        accueillir.adressemail = hebergeur
        
        accueillir.save()
        
        
        print("date debut : " + accueillir.get_datedebut())
        print("date fin : " + accueillir.get_datefin())
        print("id jeune : " + accueillir.get_idpersonne().get_idpersonne())
        print("id hebergeur : " + accueillir.get_idpersonne_1().get_idpersonne())
        print("mail : " + str(accueillir.get_adressemail()))

        
    # else:
    template = loader.get_template('webApplication/dispatch.html')
    start_date = datetime.today()
    delai = timedelta(7)
    end_date = start_date + delai
    jeunes_fin_hebergement_list = Accueillir.objects.all().filter(datefin__lte=end_date) 
    hebergeurs_list = Hebergeur.objects.all()
    context = {
        'jeunes_fin_hebergement_list' : jeunes_fin_hebergement_list,
        'hebergeurs_list' : hebergeurs_list,
        'today' : start_date
    }
    return HttpResponse(template.render(context, request))


# Méthode associée à la page listeHebergeurs
# Cette méthode permet de récupérer la totalité des hébergeurs dans la base de données
# Méthode à paramètre facultatif: si un id est donné en paramètre, on cherche l'hébergeur correspondant à cet id pour en afficher le détail du profil
def listeHebergeurs(request, hebergeur_id=None):
    hebergeurs_list = Hebergeur.objects.all()
    template = loader.get_template('webApplication/listeHebergeurs.html')
    context = {}
    context['hebergeurs_list'] = hebergeurs_list

    if hebergeur_id != None:
        hebergeurSelection = get_object_or_404(Hebergeur, idpersonne=hebergeur_id)
        context['hebergeurSelection'] = hebergeurSelection

    return HttpResponse(template.render(context, request))

# Méthode associée à la page listeJeunes
# Cette méthode permet de récupérer la totalité des jeunes dans la base de données
# Méthode à paramètre facultatif: si un id est donné en paramètre, on cherche le jeune correspondant à cet id pour en afficher le détail du profil
def listeJeunes(request, jeune_id=None):
    start_date = datetime.today()
    jeunes_list = Jeune.objects.all()
    jeunes_heberges_list = Accueillir.objects.values_list('idpersonne', flat=True).filter(datefin__gte=start_date)
    template = loader.get_template('webApplication/listeJeunes.html')
    context = {}
    context['jeunes_list'] = jeunes_list
    context['jeunes_heberges_list'] = jeunes_heberges_list

    if jeune_id != None:
        jeuneSelection = get_object_or_404(Jeune, idpersonne=jeune_id)
        liste_langue_parler = Parler.objects.all().filter(idpersonne=jeune_id)
        context['jeuneSelection'] = jeuneSelection
        context['liste_langue_parler'] = liste_langue_parler

    return HttpResponse(template.render(context, request))

# Méthode associée à la page de connexion
def connexion(request):
    error = False
    if request.method == "POST":
        user = request.POST['user']
        pwd = request.POST['pwd']
        user_obj = authenticate(username=user, password=pwd)

        if user_obj is not None:
            login(request, user_obj)
            return render(request, 'webApplication/index.html', locals())
    return render(request, 'webApplication/connexion.html', locals())

def deleteHebergeur(request, pk):
    hebergeurSelection = get_object_or_404(Hebergeur, idpersonne=pk)
    hebergeurSelection.delete()
    template = loader.get_template('webApplication/listeHebergeurs.html')
    context = {}
    context['hebergeurs_list'] = Hebergeur.objects.all()
    return HttpResponse(template.render(context, request))

def deleteJeune(request, pk):
    jeuneSelection = get_object_or_404(Jeune, idpersonne=pk)
    jeuneSelection.delete()
    template = loader.get_template('webApplication/listeJeunes.html')
    context = {}
    context['jeunes_list'] = Jeune.objects.all()
    return HttpResponse(template.render(context, request))








