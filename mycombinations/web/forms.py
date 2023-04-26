from django.forms import ModelForm
from web.models import Combination

class Combinations(ModelForm):
    class Meta:
        model= Combination
        fields= ['name','alcohol','mix','image']