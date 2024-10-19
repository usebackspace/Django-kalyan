from django.shortcuts import render
from . forms import MarvelForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        mf=MarvelForm(request.POST)
        if mf.is_valid():
            print('name....',mf.cleaned_data['name'])
            print('email....',mf.cleaned_data['email'])
        mf =MarvelForm()
    else:
        mf = MarvelForm()
    return render(request,'core/index.html',{'mf':mf})