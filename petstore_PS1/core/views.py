from django.shortcuts import render
from django.views import View
from . models import Customer,Pet,Order,Cart

# Create your views here.
# def home(request):
#     return render(request, 'core/home.html')

# --- Clased Based View of Home ---
class HomeView(View):
    def get(self,request):
        return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')

# --- Function Based View of dog_categories---
# def dog_categories(request):
#     return render(request,'core/dog_categories.html')

#--- Class Based View of dog_categories ---
class DogCategoriesView(View):
    def get(self,request):
        dog_category = Pet.objects.filter(category='DOG')  # we are using filter function of queryset, that will filter those data whose category belongs to dog
        return render(request,'core/dog_categories.html',{'dog_category':dog_category})


# --- Function Based View of cat_categories---
# def cat_categories(request):
#     return render(request,'core/cat_categories.html')

#--- Class Based View of cat_categories ---
class CatCategoriesView(View):
    def get(self,request):
        cat_category = Pet.objects.filter(category='CAT')  # we are using filter function of queryset, that will filter those data whose category belongs to dog
        return render(request,'core/cat_categories.html',{'cat_category':cat_category})


def bird_categories(request):
    return render(request,'core/bird_categories.html')

# def pet_details(request):
#     return render(request,'core/pet_details.html')

class PetDetailView(View):
    def get(self,request,id):     # id = It will fetch id of particular pet 
        pet_detail = Pet.objects.get(pk=id)

        #------ code for caculate percentage -----
        if pet_detail.discounted_price !=0:    # fetch discount price of particular pet
            percentage = int(((pet_detail.selling_price-pet_detail.discounted_price)/pet_detail.selling_price)*100)
        else:
            percentage = 0
        # ------ code end for caculate percentage ---------
            
        return render(request,'core/pet_details.html',{'pd':pet_detail,'percentage':percentage})
