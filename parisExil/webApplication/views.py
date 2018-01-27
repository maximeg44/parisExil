from django.http import HttpResponse
from django.template import loader
from .models import Jeune
from lib2to3.fixes.fix_input import context

def index(request):
    jeunes_fin_hebergement_list = Jeune.objects.all()
    template = loader.get_template('webApplication/index.html')
    context = {
        'jeunes_fin_hebergement_list' : jeunes_fin_hebergement_list,
        }
    return HttpResponse(template.render(context, request))