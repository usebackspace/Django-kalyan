from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from . forms import SignUpForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# Create your views here.
def signup(request):
    if request.method == 'POST':
        mf=SignUpForm(request.POST)
        if mf.is_valid():
            mf.save()
        return redirect('signup')
    else:
        mf=SignUpForm()
    return render(request,'core/signup.html',{'mf':mf})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            mf=AuthenticationForm(request,data=request.POST)
            if mf.is_valid():
                u_username = mf.cleaned_data['username']
                u_password = mf.cleaned_data['password']
                user = authenticate(username=u_username,password=u_password)
                if user is not None:
                    login(request,user)
                    return redirect('profile')
        else:
            mf=AuthenticationForm()
        return render(request,'core/login.html',{'mf':mf})
    else:
        return redirect('profile')
    

def profile(request):
    if request.user.is_authenticated:
        return render(request,'core/profile.html')
    else:
        return redirect('login')


def user_logout(request):
    logout(request)
    return redirect('login')


def pcf(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            mf= PasswordChangeForm(user=request.user,data=request.POST)
            if mf.is_valid():
                mf.save()
                update_session_auth_hash(request,mf.user)
                return redirect('profile')
        else:
            mf=PasswordChangeForm(user=request.user)
            return render(request,'core/pcf.html',{'mf':mf})
    else:
        return redirect('login')
    


def spf(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            mf= SetPasswordForm(user=request.user,data=request.POST)
            if mf.is_valid():
                mf.save()
                update_session_auth_hash(request,mf.user)
                return redirect('profile')
        else:
            mf=SetPasswordForm(user=request.user)
            return render(request,'core/spf.html',{'mf':mf})
    else:
        return redirect('login')
    

