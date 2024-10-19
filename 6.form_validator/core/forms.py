from  django import forms
from django.core import validators

def start_with_s(val):
    x=val[0]
    if x.isdigit():
        raise forms.ValidationError('Name Doen"t start with Number')
    
    if x =='s' or x=='S':
        raise forms.ValidationError('S is rectricted')

class MarvelForm(forms.Form):
    # name= forms.CharField(validators=[validators.MaxLengthValidator(5)])
    name= forms.CharField(validators=[start_with_s])
   