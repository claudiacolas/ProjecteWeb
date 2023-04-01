from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from web.models import Brand, Alcohol, Mix, Combination

# Create your views here.

def principal(request):
    Combination = Combination.objects.all()
    return render(request, 'web/index.html', {"combination": combination})
    
def combination(request, combination_id):
    Combination = Combination.objects.get(pk=combination_id)
    return render(request, 'web/combination.html', {"combination": combination})
class AlcoholView(generic.DetailView):
    model = Alcohol
    template_name = 'web/alcohol.html'
class MixView(generic.DetailView):
    model = Mix
    template_name = 'web/mix.html'