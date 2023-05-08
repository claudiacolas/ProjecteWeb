from django.urls import path
from django.utils import timezone
from django.views.generic import ListView
from django.conf import settings
from django.views.static import serve


from web.forms import CombinationForm
from web.views import CombinationDetail, CombinationCreate, LoginRequiredCheckIsOwnerUpdateView
from web.models import Combination

app_name = 'web'

urlpatterns = [
    # List latest 5 combinations: /mycombinations/
    path('',
         ListView.as_view(
             queryset=Combination.objects.filter(date__lte=timezone.now()).order_by('-date')[:5],
             context_object_name='latest_combination_list',
             template_name='combination_list.html'),
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