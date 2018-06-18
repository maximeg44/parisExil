from django.http import HttpResponse
from django.template import loader
from .models import Personne, Jeune, Accueillir, Parler, Membre, Hebergeur, Disponibilite, Langue, Ecole, Avocat, Nationalite
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from _datetime import timedelta
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import re

# Méthode associé à la page d'accueil du site
# Elle permet de récupérer un ensemble de jeune n'était plus hébergé dans les 7 jours à venir..
@login_required
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
@login_required
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
        
        
        """Conversion de la date de debut au bon format"""
        dateDebut = request.POST["dateDebut"]
        day = dateDebut[:2]
        month = dateDebut[3:5]
        year = '20' + dateDebut[6:8]
        dateDebut = year + '-' + month + '-' + day
        date_object_debut = datetime.strptime(dateDebut, "%Y-%m-%d")
        
        """Conversion de la date de fin au bon format"""
        dateFin = request.POST["dateFin"]
        day = dateFin[:2]
        month = dateFin[3:5]
        year = '20' + dateFin[6:8]
        dateFin = year + '-' + month + '-' + day
        date_object_fin = datetime.strptime(dateFin, "%Y-%m-%d")

        
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
    delai = timedelta(7)
    end_date = start_date + delai
    jeunes_fin_hebergement_list = Jeune.objects.all()  # Accueillir.objects.all().filter(datefin__lte=end_date)
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
@login_required
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
@login_required
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

# Méthode permettant de générer le formulaire de modification d'un hébergeur
@login_required
def hebergeurCreateOrUpdate(request, hebergeur_id=None):
    template = loader.get_template('webApplication/formulaireHebergeur.html')
    context = {}
    if hebergeur_id != None:
        hebergeurSelection = get_object_or_404(Hebergeur, idpersonne=hebergeur_id)
        context['hebergeurSelection'] = hebergeurSelection
        try:
            disponibiliteSelection = Disponibilite.objects.get(adressemail=hebergeurSelection.adressemail)
        except Disponibilite.DoesNotExist:
            disponibiliteSelection = None
        context['disponibilite'] = disponibiliteSelection

    return HttpResponse(template.render(context, request))

# Méthode permettant d'enregistrer dans la BDD les valeurs des champs du formulaire d'un hébergeur
@login_required
def modifyHebergeur(request):
    # Récupération des données du formulaire
    if request.method == "POST":

        nom = request.POST['nom']
        prenom = request.POST['prenom']
        adresse = request.POST['adresse']
        telephone = request.POST['telephone']
        mail = request.POST['mail']
        facebook = request.POST['facebook']

        if request.POST['signatureCharte'] == "True":
            signatureCharte = True
        else:
            signatureCharte = False
            
        capaciteAccueil = request.POST['capaciteAccueil']
        nbLitsSimples = request.POST['nbLitsSimples']
        nbLitsDoubles = request.POST['nbLitsDoubles']
        disponibiliteDebut = request.POST['dispoDebut']
        disponibiliteFin = request.POST['dispoFin']
        commentaires = request.POST['commentaires']

        # Si la personne existe, on la met à jour
        if request.POST['idpersonne']:
            hebergeurId = request.POST['idpersonne']
            objPersonne, personneCreated = Personne.objects.update_or_create(idpersonne=hebergeurId, defaults={'nom' : nom, 'prenom' : prenom, 'numtel' : telephone, 'commentaire' : commentaires, })
        # Si elle n'existe pas, on la crée
        else:
            objPersonne = Personne.objects.create(nom=nom, prenom=prenom, numtel=telephone, commentaire=commentaires)
        # On associe l'hébergeur à une personne
        objHebergeur, hebergeurCreated = Hebergeur.objects.update_or_create(adressemail=mail, defaults={'idpersonne' : objPersonne, 'facebook' : facebook, 'signaturecharte' : signatureCharte, 'adressepostale' : adresse, 'capaciteaccueil' : capaciteAccueil, 'nblitsimple' : nbLitsSimples, 'nblitdouble' : nbLitsDoubles, })

        # On vérifie que les dates ne sont pas nulles
        matchDateDebut = re.match(r"\d{4}-\d{2}-\d{2}", disponibiliteDebut)
        matchDateFin = re.match(r"\d{4}-\d{2}-\d{2}", disponibiliteFin)

        # Si on a deux dates correctes, on ajoute les disponibilités dans la BDD
        if matchDateDebut and matchDateFin:
            Disponibilite.objects.select_related().filter(adressemail=mail).update(datedebut=disponibiliteDebut, datefin=disponibiliteFin)
        else:
            Disponibilite.objects.select_related().filter(adressemail=mail).update(datedebut=None, datefin=None)

    return redirect('listeHebergeurs')        


# Méthode permettant de générer le formulaire de modification d'un hébergeur
@login_required
def jeuneCreateOrUpdate(request, jeune_id=None):
    template = loader.get_template('webApplication/formulaireJeune.html')
    context = {}
    if jeune_id != None:
        jeuneSelection = get_object_or_404(Jeune, idpersonne=jeune_id)
        context['jeuneSelection'] = jeuneSelection

    return HttpResponse(template.render(context, request))

# Méthode permettant d'enregistrer dans la BDD les valeurs des champs du formulaire d'un hébergeur
@login_required
def modifyJeune(request):
    # Récupération des données du formulaire
    if request.method == "POST":

        nom = request.POST['nom']
        prenom = request.POST['prenom']
        telephone = request.POST['telephone']
        dateNaissance = request.POST['dateNaissance']
        datePriseEnCharge = request.POST['datePriseEnCharge']
        signalePar = request.POST['signalePar']
        suiviPar = request.POST['suiviPar']

        if request.POST['suiviadji'] == "True":
            suiviadji = True
        else:
            suiviadji = False

        nomJuge = request.POST['nomJuge']

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
            testOsseux = True
        else:
            testOsseux = False

        sante = request.POST['sante']
        commentaires = request.POST['commentaires']

        # On traite les dates dans le cas ou une date du formulaire n'ai pas été remplie
        if not re.match(r"\d{4}-\d{2}-\d{2}", dateNaissance):
            dateNaissance = None

        if not re.match(r"\d{4}-\d{2}-\d{2}", datePriseEnCharge):
            datePriseEnCharge = None

        # Si la personne existe, on la met à jour
        if request.POST['idpersonne']:
            jeuneId = request.POST['idpersonne']
            objPersonne, personneCreated = Personne.objects.update_or_create(idpersonne=jeuneId, defaults={'nom' : nom, 'prenom' : prenom, 'numtel' : telephone, 'commentaire' : commentaires, })
        # Si elle n'existe pas, on la crée
        else:
            objPersonne = Personne.objects.create(nom=nom, prenom=prenom, numtel=telephone, commentaire=commentaires)
        
        # On associe le jeune à une personne
        objJeune, jeuneCreated = Jeune.objects.update_or_create(idpersonne=objPersonne, defaults={'datenaissance' : dateNaissance, 'datepriseencharge' : datePriseEnCharge, 'signalerpar' : signalePar, 'suivipar' : suiviPar, 'suiviadji' : suiviadji, 'nomjuge' : nomJuge, 'demie' : demie, 'recours' : recours, 'appel' : appel, 'testosseux' : testOsseux, 'sante' : sante, 'idecole' : get_object_or_404(Ecole, idecole=1), 'idavocat' : get_object_or_404(Avocat, idavocat=1), 'pays' : get_object_or_404(Nationalite, pays="France")})

    return redirect('listeJeunes')        


# Méthode associée à la page de connexion
@login_required
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
@login_required
def deleteHebergeur(request, pk):
    hebergeurSelection = get_object_or_404(Hebergeur, idpersonne=pk)
    hebergeurSelection.delete()
    template = loader.get_template('webApplication/listeHebergeurs.html')
    context = {}
    context['hebergeurs_list'] = Hebergeur.objects.all()
    return HttpResponse(template.render(context, request))

# Méthode qui permet de supprimer le jeune séléctionné
@login_required
def deleteJeune(request, pk):
    jeuneSelection = get_object_or_404(Jeune, idpersonne=pk)
    jeuneSelection.delete()
    template = loader.get_template('webApplication/listeJeunes.html')
    context = {}
    context['jeunes_list'] = Jeune.objects.all()
    return HttpResponse(template.render(context, request))







