
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
from django.urls import path, include
from django.contrib.auth import views
from django.views.generic import RedirectView
from django.views.static import serve
from django.conf import settings

import web.views

urlpatterns = [
    path('', web.views.principal, name='Principal'),
    path('combination/<int:combination_id>', web.views.combination, name='Combination'),
    path('alcohol.html',web.views.Alcohols , name = 'Alcohols'),
    path('specificalcohol/<int:pk>', web.views.AlcoholView.as_view(), name='Alcohol'),
    path('brand.html', web.views.Brands , name='Brands'),
    path('brand/<int:pk>', web.views.BrandView.as_view(), name='Brand'),
    path('mix.html',web.views.Mixs , name = 'Mixs'),
    path('mix/<int:pk>', web.views.MixView.as_view(), name='Mix'),
    path("admin/", admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
]
