from django.contrib import admin
from .models import Nationalite, Hebergeur, Membre, Jeune, Langue, Avocat, Ecole, Disponibilite

admin.site.register(Nationalite)
admin.site.register(Hebergeur)
admin.site.register(Membre)
admin.site.register(Jeune)
admin.site.register(Langue)
admin.site.register(Avocat)
admin.site.register(Ecole)
admin.site.register(Disponibilite)

