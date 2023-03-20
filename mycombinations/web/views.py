from django.shortcuts import render
from django.http import HttpResponse

from web.models import Brand, Alcohol, Mix, Combination

# Create your views here.

def principal(request):
    brands = Brand.objects.all()
    return render(request, 'web/index.html', {"brands": brands})
    
def brand(request, brand_id):
    brand = Brand.objects.get(pk=brand_id)
    return render(request, 'web/brand.html', {"brand": brand})
