from django.forms import ModelForm
from .models import Brand, Alcohol, Mix, Combination

class BrandForm(ModelForm):
    class Meta:
        model = Brand
        exclude = ('user', 'date',)

class AlcoholForm(ModelForm):
    class Meta:
        model = Alcohol
        exclude = ('user', 'date')

class MixForm(ModelForm):
    class Meta:
        model = Mix
        exclude = ('user', 'date')

class CombinationForm(ModelForm):
    class Meta:
        model = Combination
        exclude = ('user', 'date')