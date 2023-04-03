
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from web.models import Brand, Alcohol, Mix, Combination

# Create your views here.

def principal(request):
    combinations = Combination.objects.all()
    return render(request, 'web/index.html', {"combinations": combinations})
    
def combination(request, combination_id):
    combination = Combination.objects.get(pk=combination_id)
    return render(request, 'web/combination.html', {"combination": combination})

def Alcohols(request):
    alcohols = Alcohol.objects.all()
    return render(request, 'web/alcohol.html', {"alcohols": alcohols})

def Mixs(request):
    mixs= Mix.objects.all()
    return render(request, 'web/mix.html', {'mixs': mixs})

def Brands(request):
    brands= Brand.objects.all()
    return render(request, 'web/brand.html', {'brands': brands})

class AlcoholView(generic.DetailView):
    model = Alcohol
    template_name = 'web/specificalcohol.html'

class MixView(generic.DetailView):
    model = Mix
    template_name = 'web/specificmix.html'

class BrandView(generic.DetailView):
    model = Brand
    template_name = 'web/specificbrand.html'
