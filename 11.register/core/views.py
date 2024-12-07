from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . forms import SignUpForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        mf=SignUpForm(request.POST)
        if mf.is_valid():
            mf.save()
        return redirect('index')
    else:
        mf=SignUpForm()
    return render(request,'core/index.html',{'mf':mf})