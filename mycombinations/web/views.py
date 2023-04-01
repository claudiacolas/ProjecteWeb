from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views import generic

from web.models import Brand, Alcohol, Mix, Combination

# Create your views here.

def principal(request):
    combinations = Combination.objects.all()
    return render(request, 'web/index.html', {"combination": Combination})
    
def brand(request, brand_id):
    try:
        brand = Brand.objects.get(pk=brand_id)
    except Brand.DoesNotExist:
        raise Http404("This brand doesn't exist.")
    return render(request, 'web/brand.html', {"brand": brand})

def alcohol(request, alchohol_id):
    try:
        alcohol=Alcohol.objects.get(pk=alchohol_id)
    except Alcohol.DoesNotExist:
        raise Http404("This alchohol doesn't exist.")
    return render(request, 'web/alcohol.html', {"alcohol":alcohol})

def mix(request, mix_id):
    try:
        mix= Mix.objects.get(pk=mix_id)
    except:
        raise Http404("This mix doesn't exist.")
    return render(request, 'web/mix.html',{"mix":mix})

class CombinationView(generic.DeleteView):
    model=Combination
    template_name='web/combination.html'
