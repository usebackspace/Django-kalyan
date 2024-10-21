from django.shortcuts import render,redirect
from . forms import MarvelForm
from . models import Marvel
# Create your views here.
def index(request):
    if request.method == 'POST':
        mf=MarvelForm(request.POST)
        if mf.is_valid():
            mf.save()
            return redirect('index')
    else:
        mf = MarvelForm()
    return render(request,'core/index.html',{'mf':mf})