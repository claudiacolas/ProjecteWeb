from django.urls import path
from django.utils import timezone
from django.views.generic import ListView
from django.conf import settings
from django.views.static import serve

from .forms import *
from .views import *
from .models import *

app_name = 'web'

urlpatterns = [
    # List latest 5 combinations: /mycombinations/
    path('',
         ListView.as_view(
             queryset=Combination.objects.filter(date__lte=timezone.now()).order_by('-date')[:5],
             context_object_name='latest_combination_list',
             template_name='web/combination_list.html'),
         name='combination_list'),

    # Combination details, ex.: /mycombinations/combinations/1/
    path('combinations/<int:pk>',
         CombinationDetail.as_view(
            template_name='web/combination_detail.html'
         ),
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

     # Delete a /mycombinations/alcohols/<int:pk>/delete,
     path('combinations/<int:pk>/delete',
          CombinationDelete.as_view(),
          name='combination_delete'),

     # Alcohol list of instances a /mycombinations/alcohols,
     path('brands/',
          BrandList.as_view(),
          name='brand_list'),

    # Brands details, ex.: /mycombinations/brands/1/
    path('brands/<int:pk>',
         BrandDetail.as_view(),
         name='brand_detail'),

    # Create a brand, /mycombinations/brands/create/
    path('brands/create',
         BrandCreate.as_view(),
         name='brand_create'),

     # Delete a /mycombinations/brand/<int:pk>/delete,
     path('brands/<int:pk>/delete',
          BrandDelete.as_view(),
          name='brand_delete'),
     
     # Alcohol list of instances a /mycombinations/alcohols,
     path('mixs/',
          MixList.as_view(),
          name='mix_list'),


    # Mixs details, ex.: /mycombinations/mixs/1/
    path('mixs/<int:pk>',
         MixDetail.as_view(),
         name='mix_detail'),
  # Mixs details, ex.: /mycombinations/mixs/1/
   
    # Create a mix, /mycombinations/mixs/create/
    path('mixs/create',
         MixCreate.as_view(),
         name='mix_create'),

     # Delete a /mycombinations/mixs/<int:pk>/delete,
     path('mixs/<int:pk>/delete',
          MixDelete.as_view(),
          name='mix_delete'),

     # Alcohol list of instances a /mycombinations/alcohols,
     path('alcohols/',
          AlcoholList.as_view(),
          name='alcohol_list'),

    # Alcohols details, ex.: /mycombinations/alcohols/1/
    path('alcohols/<int:pk>',
         AlcoholDetail.as_view(
             model=Alcohol,
            template_name='web/alcohol_detail.html'),
        name='alcohol_detail'),

    # Create an alcohol, /mycombinations/alcohols/create/
    path('alcohols/create',
         AlcoholCreate.as_view(),
         name='alcohol_create'),

     # Delete a /mycombinations/alcohols/<int:pk>/delete,
     path('alcohols/<int:pk>/delete',
          AlcoholDelete.as_view(),
          name='alcohol_delete'),

    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT, }),

    # Create a combination review, ex.: /mycombinations/combinations/1/reviews/create/
    path('combinations/<int:pk>/reviews/create',
        review,
        name='review_create'),
]
