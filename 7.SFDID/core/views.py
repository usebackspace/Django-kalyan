from django.shortcuts import render
from . forms import MarvelForm
from . models import Marvel
# Create your views here.
def index(request):
    if request.method == 'POST':
        mf=MarvelForm(request.POST)
        if mf.is_valid():
            nm=mf.cleaned_data['name']
            hn=mf.cleaned_data['heroic_name']
            Marvel(name=nm,heroic_name=hn).save()
        mf =MarvelForm()
    else:
        mf = MarvelForm()
    return render(request,'core/index.html',{'mf':mf})