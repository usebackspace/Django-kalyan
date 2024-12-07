from django.urls import path
from . import views
urlpatterns = [
    path('',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('pcf/',views.pcf,name='pcf'),
    path('spf/',views.spf,name='spf'),
]
