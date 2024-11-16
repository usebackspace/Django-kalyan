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
        mm= Marvel.objects.all
    return render(request,'core/index.html',{'mf':mf,'mm':mm})

def m_delete(request,id):
    mf= Marvel.objects.get(pk=id)
    mf.delete()
    return redirect('index')

def m_update(request,id):
    if request.method=='POST':
        mm= Marvel.objects.get(pk=id)
        mf= MarvelForm(request.POST,instance=mm)
        if mf.is_valid():
            mf.save()
    else:    
        mm= Marvel.objects.get(pk=id)
        mf=MarvelForm(instance=mm)
    return render(request,'core/update.html',{'mf':mf})