
"""mycombinations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.utils import timezone
from django.contrib.auth import views
from django.views.generic import DetailView, ListView
from django.conf import settings
from django.views.static import serve

#from web.models import *
from mycombinations.forms import BrandForm, MixForm, AlcoholForm, CombinationForm
from mycombinations.web.views import LoginRequiredCheckIsOwnerUpdateView
from web.views import Principal, combination, Alcohols, Mixs, Brands, AlcoholView, MixView, BrandView, \
    CombinationDetail, CombinationCreate, AlcoholCreate, MixCreate, BrandCreate
from web.models import Brand, Mix, Alcohol, Combination

app_name = 'mycombinations'

urlpatterns = [
    path('', Principal, name='Principal'),
    path("admin/", admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),

    # List latest 5 combinations: /mycombinations/
    path('',
        ListView.as_view(
            queryset=Combination.objects.filter(date__lte=timezone.now()).order_by('-date')[:5],
            context_object_name='latest_combination_list',
            template_name='mycombinations/combination_list.html'),
        name='combination_list'),

    # Combination details, ex.: /mycombinations/combinations/1/
    path('combinations/<int:pk>',
         CombinationDetail.as_view(),
         name='combination_detail'),
    
    # Create a combination, /mycombinations/combinations/create/
    path('combinations/create',
        CombinationCreate.as_view(),
        name='combination_create'),
    
    # Edit combination details, ex.: /mycombinations/combinations/1/edit/
    path('combinations/<int:pk>/edit',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Combination,
            form_class=CombinationForm),
        name='combination_edit'),
    
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT, })

]
