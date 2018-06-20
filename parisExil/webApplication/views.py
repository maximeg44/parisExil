from django.http import HttpResponse
from django.template import loader
from .models import Personne, Jeune, Accueillir, Parler, Hebergeur, Disponibilite, Ecole, Avocat, Nationalite
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from _datetime import timedelta
from django.contrib.auth import authenticate, login
import re

# Méthode associé à la page d'accueil du site
# Elle permet de récupérer un ensemble de jeune n'était plus hébergé dans les 7 jours à venir..
def index(request):
    start_date = datetime.today()
    delai = timedelta(7)
    end_date = start_date + delai
    jeunes_fin_hebergement_list = Accueillir.objects.all().filter(datefin__range=[start_date,end_date])
    template = loader.get_template('webApplication/index.html')
    context = {
        'jeunes_fin_hebergement_list' : jeunes_fin_hebergement_list,
        }
    return HttpResponse(template.render(context, request))

# Méthode associée à la page de la liste des jeunes
# Elle permet de récupérer les informations d'un jeune séléctionné
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
def dispatcher(request):
    if request.method == 'POST':
        accueillir = Accueillir()
        hebergeur = Hebergeur.objects.get(idpersonne=request.POST["selectHebergeur"])
        jeune = Jeune()
        
        hebergeur = Hebergeur.objects.get(idpersonne=request.POST["selectHebergeur"])
        jeune.idpersonne = Personne(request.POST["selectJeune"])
        hebergeur.idpersonne = Personne(request.POST["selectHebergeur"])
        
        
        """Conversion de la date de debut au bon format"""
        date_debut =  request.POST["dateDebut"]
        day = date_debut[:2]
        month = date_debut[3:5]
        year = '20' + date_debut[6:8]
        date_debut = year + '-' + month + '-' + day
        date_object_debut = datetime.strptime(date_debut, "%Y-%m-%d")
        
        """Conversion de la date de fin au bon format"""
        date_fin = request.POST["dateFin"]
        day = date_fin[:2]
        month = date_fin[3:5]
        year = '20' + date_fin[6:8]
        date_fin = year + '-' + month + '-' + day
        date_object_fin = datetime.strptime(date_fin, "%Y-%m-%d")

        
        accueillir.datedebut = date_object_debut
        accueillir.datefin = date_object_fin
        accueillir.idpersonne = jeune.get_idpersonne()
        accueillir.idpersonne_1 = hebergeur.get_idpersonne()        
        accueillir.idpersonne_2 = Personne(request.user.id)        
        accueillir.adressemail = hebergeur
        
        accueillir.save(force_insert=True)
        
    # else:
    template = loader.get_template('webApplication/dispatch.html')
    start_date = datetime.today()
    jeunes_fin_hebergement_list = Jeune.objects.all()
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
        hebergeur_selection = get_object_or_404(Hebergeur, idpersonne=hebergeur_id)
        context['hebergeurSelection'] = hebergeur_selection

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
        jeune_selection = get_object_or_404(Jeune, idpersonne=jeune_id)
        liste_langue_parler = Parler.objects.all().filter(idpersonne=jeune_id)
        context['jeuneSelection'] = jeune_selection
        context['liste_langue_parler'] = liste_langue_parler

    return HttpResponse(template.render(context, request))

#Méthode permettant de générer le formulaire de modification d'un hébergeur
def hebergeurCreateOrUpdate(request, hebergeur_id=None):
    template = loader.get_template('webApplication/formulaireHebergeur.html')
    context = {}
    if hebergeur_id != None:
        hebergeur_selection = get_object_or_404(Hebergeur, idpersonne=hebergeur_id)
        context['hebergeurSelection'] = hebergeur_selection
        try:
            disponibilite_selection = Disponibilite.objects.get(adressemail=hebergeur_selection.adressemail)
        except Disponibilite.DoesNotExist:
            disponibilite_selection = None
        context['disponibilite'] = disponibilite_selection

    return HttpResponse(template.render(context, request))

#Méthode permettant d'enregistrer dans la BDD les valeurs des champs du formulaire d'un hébergeur
def modifyHebergeur(request):
    #Récupération des données du formulaire
    if request.method == "POST":

        nom = request.POST['nom']
        prenom = request.POST['prenom']
        adresse = request.POST['adresse']
        telephone = request.POST['telephone']
        mail = request.POST['mail']
        facebook = request.POST['facebook']

        if request.POST['signatureCharte'] == "True":
            signature_charte = True
        else:
            signature_charte = False
            
        capacite_accueil = request.POST['capaciteAccueil']
        nb_lits_simples = request.POST['nbLitsSimples']
        nb_lits_doubles = request.POST['nbLitsDoubles']
        disponibilite_debut = request.POST['dispoDebut']
        disponibilite_fin = request.POST['dispoFin']
        commentaires = request.POST['commentaires']

        #Si la personne existe, on la met à jour
        if request.POST['idpersonne']:
            hebergeur_id = request.POST['idpersonne']
            obj_personne, personne_created = Personne.objects.update_or_create(idpersonne = hebergeur_id, defaults={'nom' : nom, 'prenom' : prenom, 'numtel' : telephone, 'commentaire' : commentaires,})
        #Si elle n'existe pas, on la crée
        else:
            obj_personne = Personne.objects.create(nom = nom, prenom = prenom, numtel = telephone, commentaire = commentaires)
        #On associe l'hébergeur à une personne
        obj_hebergeur, hebergeurCreated = Hebergeur.objects.update_or_create(adressemail = mail, defaults={'idpersonne' : obj_personne, 'facebook' : facebook, 'signaturecharte' : signature_charte, 'adressepostale' : adresse, 'capaciteaccueil' : capacite_accueil, 'nblitsimple' : nb_lits_simples, 'nblitdouble' : nb_lits_doubles,})

        #On vérifie que les dates ne sont pas nulles
        match_date_debut = re.match(r"\d{4}-\d{2}-\d{2}",disponibilite_debut)
        match_date_fin = re.match(r"\d{4}-\d{2}-\d{2}",disponibilite_fin)

        #Si on a deux dates correctes, on ajoute les disponibilités dans la BDD
        if match_date_debut and match_date_fin:
            objDispo = Disponibilite.objects.update_or_create(adressemail = obj_hebergeur, defaults={'datedebut' : disponibilite_debut, 'datefin' : disponibilite_fin})
        else:
            Disponibilite.objects.select_related().filter(adressemail = obj_hebergeur).delete()

    return redirect('listeHebergeurs')        


#Méthode permettant de générer le formulaire de modification d'un hébergeur
def jeuneCreateOrUpdate(request, jeune_id=None):
    template = loader.get_template('webApplication/formulaireJeune.html')
    context = {}
    if jeune_id != None:
        jeune_selection = get_object_or_404(Jeune, idpersonne=jeune_id)
        context['jeuneSelection'] = jeune_selection

    return HttpResponse(template.render(context, request))

#Méthode permettant d'enregistrer dans la BDD les valeurs des champs du formulaire d'un hébergeur
def modifyJeune(request):
    #Récupération des données du formulaire
    if request.method == "POST":

        nom = request.POST['nom']
        prenom = request.POST['prenom']
        telephone = request.POST['telephone']
        date_naissance = request.POST['dateNaissance']
        date_prise_en_charge = request.POST['datePriseEnCharge']
        signale_par = request.POST['signalePar']
        suivi_par = request.POST['suiviPar']

        if request.POST['suiviadji'] == "True":
            suiviadji = True
        else:
            suiviadji = False

        nom_juge = request.POST['nomJuge']

        if request.POST['demie'] == "True":
            demie = True
        else:
            demie = False

        if request.POST['recours'] == "True":
            recours = True
        else:
            recours = False

        if request.POST['appel'] == "True":
            appel = True
        else:
            appel = False

        if request.POST['testOsseux'] == "True":
            test_osseux = True
        else:
            test_osseux = False

        sante = request.POST['sante']
        commentaires = request.POST['commentaires']

        #On traite les dates dans le cas ou une date du formulaire n'ai pas été remplie
        if not re.match(r"\d{4}-\d{2}-\d{2}",date_naissance):
            date_naissance = None

        if not re.match(r"\d{4}-\d{2}-\d{2}",date_prise_en_charge):
            date_prise_en_charge = None

        #Si la personne existe, on la met à jour
        if request.POST['idpersonne']:
            jeune_id = request.POST['idpersonne']
            obj_personne, personne_created = Personne.objects.update_or_create(idpersonne = jeune_id, defaults={'nom' : nom, 'prenom' : prenom, 'numtel' : telephone, 'commentaire' : commentaires,})
        #Si elle n'existe pas, on la crée
        else:
            obj_personne = Personne.objects.create(nom = nom, prenom = prenom, numtel = telephone, commentaire = commentaires)
        
        #On associe le jeune à une personne
        obj_jeune, jeune_created = Jeune.objects.update_or_create(idpersonne = obj_personne, defaults={'datenaissance' : date_naissance, 'datepriseencharge' : date_prise_en_charge, 'signalerpar' : signale_par, 'suivipar' : suivi_par, 'suiviadji' : suiviadji, 'nomjuge' : nom_juge, 'demie' : demie, 'recours' : recours, 'appel' : appel, 'testosseux' : test_osseux, 'sante' : sante, 'idecole' : get_object_or_404(Ecole, idecole=1), 'idavocat' : get_object_or_404(Avocat, idavocat=1), 'pays' : get_object_or_404(Nationalite, pays="France")})

    return redirect('listeJeunes')        


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

# Méthode qui permet de supprimer l'hébergeur séléctionné
def deleteHebergeur(request, pk):
    hebergeur_selection = get_object_or_404(Hebergeur, idpersonne=pk)
    hebergeur_selection.delete()
    template = loader.get_template('webApplication/listeHebergeurs.html')
    context = {}
    context['hebergeurs_list'] = Hebergeur.objects.all()
    return HttpResponse(template.render(context, request))

# Méthode qui permet de supprimer le jeune séléctionné
def deleteJeune(request, pk):
    jeune_selection = get_object_or_404(Jeune, idpersonne=pk)
    jeune_selection.delete()
    template = loader.get_template('webApplication/listeJeunes.html')
    context = {}
    context['jeunes_list'] = Jeune.objects.all()
    return HttpResponse(template.render(context, request))







