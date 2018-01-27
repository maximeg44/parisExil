# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Avocat(models.Model):

    def get_idavocat(self):
        return self.__idavocat


    def get_nom(self):
        return self.__nom


    def get_numtel(self):
        return self.__numtel


    def set_idavocat(self, value):
        self.__idavocat = value


    def set_nom(self, value):
        self.__nom = value


    def set_numtel(self, value):
        self.__numtel = value

    idavocat = models.AutoField(db_column='idAvocat', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='nom', max_length=250)
    numtel = models.CharField(db_column='numTel', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Avocat'
    idavocat = property(get_idavocat, set_idavocat, None, None)
    nom = property(get_nom, set_nom, None, None)
    numtel = property(get_numtel, set_numtel, None, None)


class Disponibilite(models.Model):

    def get_datedebut(self):
        return self.__datedebut


    def get_datefin(self):
        return self.__datefin


    def get_adressemail(self):
        return self.__adressemail


    def set_datedebut(self, value):
        self.__datedebut = value


    def set_datefin(self, value):
        self.__datefin = value


    def set_adressemail(self, value):
        self.__adressemail = value


    def del_datedebut(self):
        del self.__datedebut


    def del_datefin(self):
        del self.__datefin

    datedebut = models.DateField(db_column='dateDebut', primary_key=True)  # Field name made lowercase.
    datefin = models.DateField(db_column='dateFin', blank=True, null=True)  # Field name made lowercase.
    adressemail = models.ForeignKey('Hebergeur', models.DO_NOTHING, db_column='adresseMail')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Disponibilite'
        unique_together = (('datedebut', 'adressemail'),)


class Ecole(models.Model):

    def get_idecole(self):
        return self.__idecole


    def get_libelle(self):
        return self.__libelle


    def get_ville(self):
        return self.__ville


    def set_libelle(self, value):
        self.__libelle = value


    def set_ville(self, value):
        self.__ville = value

    idecole = models.AutoField(db_column='idEcole', primary_key=True)  # Field name made lowercase.
    libelle = models.CharField(db_column='libelle', max_length=250)
    ville = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'Ecole'
    idecole = property(get_idecole, None, None, None)
    libelle = property(get_libelle, set_libelle, None, None)
    ville = property(get_ville, set_ville, None, None)


class Hebergeur(models.Model):

    def get_adressemail(self):
        return self.__adressemail


    def get_facebook(self):
        return self.__facebook


    def get_signaturecharte(self):
        return self.__signaturecharte


    def get_adressepostale(self):
        return self.__adressepostale


    def get_capaciteaccueil(self):
        return self.__capaciteaccueil


    def get_nblitsimple(self):
        return self.__nblitsimple


    def get_nblitdouble(self):
        return self.__nblitdouble


    def get_idpersonne(self):
        return self.__idpersonne


    def set_adressemail(self, value):
        self.__adressemail = value


    def set_facebook(self, value):
        self.__facebook = value


    def set_signaturecharte(self, value):
        self.__signaturecharte = value


    def set_adressepostale(self, value):
        self.__adressepostale = value


    def set_capaciteaccueil(self, value):
        self.__capaciteaccueil = value


    def set_nblitsimple(self, value):
        self.__nblitsimple = value


    def set_nblitdouble(self, value):
        self.__nblitdouble = value


    def del_nblitsimple(self):
        del self.__nblitsimple


    def del_nblitdouble(self):
        del self.__nblitdouble

    adressemail = models.CharField(db_column='adresseMail', primary_key=True, max_length=250)  # Field name made lowercase.
    facebook = models.CharField(db_column='facebook', max_length=250, blank=True, null=True)
    signaturecharte = models.IntegerField(db_column='signatureCharte')  # Field name made lowercase.
    adressepostale = models.CharField(db_column='adressePostale', max_length=250)  # Field name made lowercase.
    capaciteaccueil = models.IntegerField(db_column='capaciteAccueil')  # Field name made lowercase.
    nblitsimple = models.IntegerField(db_column='nbLitSimple', blank=True, null=True)  # Field name made lowercase.
    nblitdouble = models.IntegerField(db_column='nbLitDouble', blank=True, null=True)  # Field name made lowercase.
    idpersonne = models.ForeignKey('Personne', models.DO_NOTHING, related_name='leHebergeur', db_column='idPersonne')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hebergeur'
        unique_together = (('adressemail', 'idpersonne'),)


class Jeune(models.Model):

    def get_datenaissance(self):
        return self.__datenaissance


    def get_datepriseencharge(self):
        return self.__datepriseencharge


    def get_signalerpar(self):
        return self.__signalerpar


    def get_suivipar(self):
        return self.__suivipar


    def get_suiviadji(self):
        return self.__suiviadji


    def get_nomjuge(self):
        return self.__nomjuge


    def get_demie(self):
        return self.__demie


    def get_recours(self):
        return self.__recours


    def get_appel(self):
        return self.__appel


    def get_testosseux(self):
        return self.__testosseux


    def get_sante(self):
        return self.__sante


    def get_idpersonne(self):
        return self.__idpersonne


    def get_idecole(self):
        return self.__idecole


    def get_idavocat(self):
        return self.__idavocat


    def get_pays(self):
        return self.__pays


    def set_datenaissance(self, value):
        self.__datenaissance = value


    def set_datepriseencharge(self, value):
        self.__datepriseencharge = value


    def set_signalerpar(self, value):
        self.__signalerpar = value


    def set_suivipar(self, value):
        self.__suivipar = value


    def set_suiviadji(self, value):
        self.__suiviadji = value


    def set_nomjuge(self, value):
        self.__nomjuge = value


    def set_demie(self, value):
        self.__demie = value


    def set_recours(self, value):
        self.__recours = value


    def set_appel(self, value):
        self.__appel = value


    def set_testosseux(self, value):
        self.__testosseux = value


    def set_sante(self, value):
        self.__sante = value


    def set_idecole(self, value):
        self.__idecole = value


    def set_idavocat(self, value):
        self.__idavocat = value


    def set_pays(self, value):
        self.__pays = value

    datenaissance = models.DateField(db_column='dateNaissance')  # Field name made lowercase.
    datepriseencharge = models.DateField(db_column='datePriseEnCharge')  # Field name made lowercase.
    signalerpar = models.CharField(db_column='signalerPar', max_length=250, blank=True, null=True)  # Field name made lowercase.
    suivipar = models.CharField(db_column='suiviPar', max_length=250, blank=True, null=True)  # Field name made lowercase.
    suiviadji = models.IntegerField(db_column='SuiviAdji')  # Field name made lowercase.
    nomjuge = models.CharField(db_column='nomJuge', max_length=250, blank=True, null=True)  # Field name made lowercase.
    demie = models.IntegerField()
    recours = models.IntegerField()
    appel = models.IntegerField()
    testosseux = models.IntegerField(db_column='testOsseux')  # Field name made lowercase.
    sante = models.CharField(db_column='sante', max_length=250, blank=True, null=True)
    idpersonne = models.OneToOneField('Personne', models.DO_NOTHING, related_name='leEnfant', db_column='idPersonne', primary_key=True)  # Field name made lowercase.
    idecole = models.ForeignKey(Ecole, models.DO_NOTHING, db_column='idEcole')  # Field name made lowercase.
    idavocat = models.ForeignKey(Avocat, models.DO_NOTHING, db_column='idAvocat')  # Field name made lowercase.
    pays = models.ForeignKey('Nationalite', models.DO_NOTHING, db_column='pays')

    class Meta:
        managed = False
        db_table = 'Jeune'
    datenaissance = property(get_datenaissance, set_datenaissance, None, None)
    datepriseencharge = property(get_datepriseencharge, set_datepriseencharge, None, None)
    signalerpar = property(get_signalerpar, set_signalerpar, None, None)
    suivipar = property(get_suivipar, set_suivipar, None, None)
    suiviadji = property(get_suiviadji, set_suiviadji, None, None)
    nomjuge = property(get_nomjuge, set_nomjuge, None, None)
    demie = property(get_demie, set_demie, None, None)
    recours = property(get_recours, set_recours, None, None)
    appel = property(get_appel, set_appel, None, None)
    testosseux = property(get_testosseux, set_testosseux, None, None)
    sante = property(get_sante, set_sante, None, None)
    idpersonne = property(get_idpersonne, None, None, None)
    idecole = property(get_idecole, set_idecole, None, None)
    idavocat = property(get_idavocat, set_idavocat, None, None)
    pays = property(get_pays, set_pays, None, None)


class Langue(models.Model):

    def get_libelle(self):
        return self.__libelle

    libelle = models.CharField(db_column='libelle', primary_key=True, max_length=250)

    class Meta:
        managed = False
        db_table = 'Langue'
    libelle = property(get_libelle, None, None, None)


class Membre(models.Model):

    def get_facebook(self):
        return self.__facebook


    def get_fonction(self):
        return self.__fonction


    def get_idpersonne(self):
        return self.__idpersonne


    def set_facebook(self, value):
        self.__facebook = value


    def set_fonction(self, value):
        self.__fonction = value

    facebook = models.CharField(db_column='facebook', max_length=250, blank=True, null=True)
    fonction = models.CharField(db_column='fonction', max_length=250, blank=True, null=True)
    idpersonne = models.OneToOneField('Personne', models.DO_NOTHING, db_column='idPersonne', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Membre'
    facebook = property(get_facebook, set_facebook, None, None)
    fonction = property(get_fonction, set_fonction, None, None)
    idpersonne = property(get_idpersonne, None, None, None)


class Nationalite(models.Model):
    pays = models.CharField(db_column='pays', primary_key=True, max_length=250)

    class Meta:
        managed = False
        db_table = 'Nationalite'
        
    def __str__(self):
        return self.pays.__str__()
    #pays = property(get_pays, set_pays, None, None)
    
    def get_pays(self):
        return self.__pays


    def set_pays(self, value):
        self.__pays = value


class Personne(models.Model):

    def get_idpersonne(self):
        return self.__idpersonne


    def get_nom(self):
        return self.__nom


    def get_prenom(self):
        return self.__prenom


    def get_numtel(self):
        return self.__numtel


    def get_commentaire(self):
        return self.__commentaire


    def set_nom(self, value):
        self.__nom = value


    def set_prenom(self, value):
        self.__prenom = value


    def set_numtel(self, value):
        self.__numtel = value


    def set_commentaire(self, value):
        self.__commentaire = value

    idpersonne = models.AutoField(db_column='idPersonne', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='nom', max_length=250)
    prenom = models.CharField(db_column='prenom', max_length=250)
    numtel = models.CharField(db_column='numTel', max_length=20)  # Field name made lowercase.
    commentaire = models.CharField(db_column='commentaire', max_length=250)

    class Meta:
        managed = False
        db_table = 'Personne'
    idpersonne = property(get_idpersonne, None, None, None)
    nom = property(get_nom, set_nom, None, None)
    prenom = property(get_prenom, set_prenom, None, None)
    numtel = property(get_numtel, set_numtel, None, None)
    commentaire = property(get_commentaire, set_commentaire, None, None)


class Accueillir(models.Model):

    def get_datedebut(self):
        return self.__datedebut


    def get_datefin(self):
        return self.__datefin


    def get_commentaire(self):
        return self.__commentaire


    def get_adressemail(self):
        return self.__adressemail


    def get_idpersonne(self):
        return self.__idpersonne


    def get_idpersonne_1(self):
        return self.__idpersonne_1


    def get_idpersonne_2(self):
        return self.__idpersonne_2


    def set_datedebut(self, value):
        self.__datedebut = value


    def set_datefin(self, value):
        self.__datefin = value


    def set_commentaire(self, value):
        self.__commentaire = value

    datedebut = models.DateField(db_column='dateDebut', blank=True, null=True)  # Field name made lowercase.
    datefin = models.DateField(db_column='dateFin', blank=True, null=True)  # Field name made lowercase.
    commentaire = models.CharField(db_column='commentaire', max_length=250, blank=True, null=True)
    adressemail = models.OneToOneField(Hebergeur, models.DO_NOTHING, db_column='adresseMail', primary_key=True)  # Field name made lowercase.
    idpersonne = models.OneToOneField(Personne, models.DO_NOTHING, related_name='Jeune', db_column='idPersonne') # Field name made lowercase.
    idpersonne_1 = models.OneToOneField(Personne, models.DO_NOTHING, related_name='Hebergeur' , db_column='idPersonne_1')  # Field name made lowercase.
    idpersonne_2 = models.OneToOneField(Personne, models.DO_NOTHING, related_name='Membre', db_column='idPersonne_2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accueillir'
        unique_together = (('adressemail', 'idpersonne', 'idpersonne_1', 'idpersonne_2'),)
    


class Apprecier(models.Model):

    def get_adressemail(self):
        return self.__adressemail


    def get_idpersonne(self):
        return self.__idpersonne


    def get_idpersonne_1(self):
        return self.__idpersonne_1

    adressemail = models.OneToOneField(Hebergeur, models.DO_NOTHING, db_column='adresseMail', primary_key=True)  # Field name made lowercase.
    idpersonne = models.OneToOneField(Personne, models.DO_NOTHING, related_name='unJeune', db_column='idPersonne')  # Field name made lowercase.
    idpersonne_1 = models.OneToOneField(Personne, models.DO_NOTHING, related_name='unHebergeur' , db_column='idPersonne_1')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'apprecier'
        unique_together = (('adressemail', 'idpersonne', 'idpersonne_1'),)



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Deprecier(models.Model):

    def get_adressemail(self):
        return self.__adressemail


    def get_idpersonne(self):
        return self.__idpersonne


    def get_idpersonne_1(self):
        return self.__idpersonne_1

    adressemail = models.OneToOneField(Hebergeur, models.DO_NOTHING, db_column='adresseMail', primary_key=True)  # Field name made lowercase.
    idpersonne = models.OneToOneField(Personne, models.DO_NOTHING, related_name='jeune' , db_column='idPersonne')  # Field name made lowercase.
    idpersonne_1 = models.OneToOneField(Personne, models.DO_NOTHING, related_name='hebergeur' , db_column='idPersonne_1')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'deprecier'
        unique_together = (('adressemail', 'idpersonne', 'idpersonne_1'),)



class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Entente(models.Model):

    def get_idpersonne(self):
        return self.__idpersonne


    def get_idpersonne_1(self):
        return self.__idpersonne_1

    idpersonne = models.OneToOneField(Personne, models.DO_NOTHING, related_name='leJeune', db_column='idPersonne', primary_key=True)  # Field name made lowercase.
    idpersonne_1 = models.OneToOneField(Personne, models.DO_NOTHING, related_name='le_Jeune', db_column='idPersonne_1')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'entente'
        unique_together = (('idpersonne', 'idpersonne_1'),)



class Mesentente(models.Model):

    def get_idpersonne(self):
        return self.__idpersonne


    def get_idpersonne_1(self):
        return self.__idpersonne_1

    idpersonne = models.OneToOneField(Personne, models.DO_NOTHING, related_name='UnJeune', db_column='idPersonne', primary_key=True)  # Field name made lowercase.
    idpersonne_1 = models.OneToOneField(Personne, models.DO_NOTHING,related_name='Un_Jeune', db_column='idPersonne_1')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mesentente'
        unique_together = (('idpersonne', 'idpersonne_1'),)
    


class Parler(models.Model):

    def get_libelle(self):
        return self.__libelle


    def get_idpersonne(self):
        return self.__idpersonne

    libelle = models.OneToOneField(Langue, models.DO_NOTHING, db_column='libelle', primary_key=True)
    idpersonne = models.ForeignKey(Personne, models.DO_NOTHING, db_column='idPersonne')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'parler'
        unique_together = (('libelle', 'idpersonne'),)

