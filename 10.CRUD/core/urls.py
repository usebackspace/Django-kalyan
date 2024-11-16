from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<int:id>',views.m_delete,name='delete'),
    path('update/<int:id>',views.m_update,name='update')
]
