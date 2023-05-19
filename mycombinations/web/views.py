from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import *
from .models import *

# Create your views here.

class AlcoholList(ListView):
    model = Alcohol
    template_name = 'web/alcohol_list.html'

    def get_context_data(self, **kwargs):
        context = super(AlcoholList, self).get_context_data(**kwargs)
        context['alcohols'] = Alcohol.objects.all() 
        return context

class BrandList(ListView):
    model = Brand
    template_name = 'web/brand_list.html'

    def get_context_data(self, **kwargs):
        context = super(BrandList, self).get_context_data(**kwargs)
        context['brands'] = Brand.objects.all() 
        return context    
    
class MixList(ListView):
    model = Mix
    template_name = 'web/mix_list.html'

    def get_context_data(self, **kwargs):
        context = super(MixList, self).get_context_data(**kwargs)
        context['mixs'] = Mix.objects.all() 
        return context

class MixDetail(generic.DetailView):
    model = Mix
    template_name = 'web/mix_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MixDetail, self).get_context_data(**kwargs)
        return context
    
class AlcoholDetail(generic.DetailView):
    model = Alcohol
    template_name = 'web/alcohol_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AlcoholDetail, self).get_context_data(**kwargs)
        return context

class BrandDetail(generic.DetailView):
    model = Brand
    template_name = 'web/brand_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BrandDetail, self).get_context_data(**kwargs)
        return context

class CombinationDetail(DetailView):
    model = Combination
    template_name = 'web/combination_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CombinationDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = CombinationReview.RATING_CHOICES
        return context
    
class CombinationCreate(LoginRequiredMixin, CreateView):
    model = Combination
    template_name = 'web/form.html'
    form_class = CombinationForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CombinationCreate, self).form_valid(form)
    
class AlcoholCreate(LoginRequiredMixin, CreateView):
    model = Alcohol
    template_name = 'web/form.html'
    form_class = AlcoholForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AlcoholCreate, self).form_valid(form)
    
class MixCreate(LoginRequiredMixin, CreateView):
    model = Mix
    template_name = 'web/form.html'
    form_class = MixForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MixCreate, self).form_valid(form)
    
class BrandCreate(LoginRequiredMixin, CreateView):
    model = Brand
    template_name = 'web/form.html'
    form_class = BrandForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BrandCreate, self).form_valid(form)
    
class BrandDelete(DeleteView):
    model = Brand

    def get_success_url(self):
        return reverse('web:combination_list')

    def post(self, request, **kwargs):
        brand_id = kwargs['pk']
        brand = get_object_or_404(Brand, id=brand_id)
        if brand.user == request.user:
            brand.delete()
        return redirect(self.get_success_url())

class MixDelete(DeleteView):
    model = Mix

    def get_success_url(self):
        return reverse('web:combination_list')

    def post(self, request, **kwargs):
        mix_id = kwargs['pk']
        mix = get_object_or_404(Mix, id=mix_id)
        if mix.user == request.user:
            mix.delete()
        return redirect(self.get_success_url())
    
class AlcoholDelete(DeleteView):
    model = Alcohol

    def get_success_url(self):
        return reverse('web:combination_list')

    def post(self, request, **kwargs):
        alcohol_id = kwargs['pk']
        alcohol = get_object_or_404(Alcohol, id=alcohol_id)
        if alcohol.user == request.user:
            alcohol.delete()
        return redirect(self.get_success_url())
    
class CombinationDelete(DeleteView):
    model = Combination

    def get_success_url(self):
        return reverse('web:combination_list')

    def post(self, request, **kwargs):
        combination_id = kwargs['pk']
        combination = get_object_or_404(Combination, id=combination_id)
        if combination.user == request.user:
            combination.delete()
        return redirect(self.get_success_url())

# Security Mixins

class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj
    
class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'web/form.html'

@login_required()
def review(request, pk):
    combination = get_object_or_404(Combination, pk=pk)
    if CombinationReview.objects.filter(combination=combination, user=request.user).exists():
        CombinationReview.objects.get(combination=combination, user=request.user).delete()
    new_review = CombinationReview(
        rating=request.POST.get('rating', 0),
        comment=request.POST['comment'],
        user=request.user,
        combination=combination)
    new_review.save()
    return HttpResponseRedirect(reverse('web:combination_detail', args=(combination.id,)))