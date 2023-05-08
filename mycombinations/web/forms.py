from django.forms import ModelForm
from .models import Brand, Alcohol, Mix, Combination

class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'type']

class AlcoholForm(ModelForm):
    class Meta:
        model = Alcohol
        fields = ['name', 'brand']

class MixForm(ModelForm):
    class Meta:
        model = Mix
        fields = ['name', 'brand']

class CombinationForm(ModelForm):
    class Meta:
        model = Combination
        fields = ['name', 'alcohol', 'mix','image']