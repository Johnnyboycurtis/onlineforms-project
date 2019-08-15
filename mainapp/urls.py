from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('createcontact/', views.createcontact, name = 'createcontact'),
    path('about/', views.about, name='about'),
    path('<int:id>/detailedview/', views.detailedview, name='detailedview')
]
