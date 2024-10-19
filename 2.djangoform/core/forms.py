from  django import forms

class MarvelForm(forms.Form):
    name = forms.CharField(label='First Name', label_suffix=' - ' ,help_text='Enter your full name.')
    city = forms.CharField(required=False,initial='NYC')
    heroic_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Favourite hero','class':'heroee'}))