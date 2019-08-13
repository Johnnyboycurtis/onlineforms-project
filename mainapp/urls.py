from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('newapp/', views.newapp, name = 'newapp'),
    path('about/', views.about, name='about')
]
