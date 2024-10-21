from  django import forms
from . models import Marvel

class MarvelForm(forms.ModelForm):
    
    class Meta:
        model = Marvel
        fields = ['name','heroic_name']