from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import *
from .models import *

# Create your views here.

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
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect('web/index.html/')

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
    def post(self, request, brand_id):
        brand = get_object_or_404(Brand, id=brand_id)
        if brand.user == request.user:
            brand.delete()
        return redirect('web/index.html')

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