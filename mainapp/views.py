from django.shortcuts import render
from .forms import UserInfoForm, LanguagesFormSet, SportsFormSet

def home(request):
    return render(request, 'mainapp/home.html')

def newapp(request):
    context = {'userinfoform': UserInfoForm}
    return render(request, 'mainapp/newapp.html', context)


def appform(request, userid):
    context = {'userinfoform': UserInfoForm, 'languagesform': LanguagesFormSet, 'sportsform': SportsFormSet}
    return render(request, 'mainapp/<userid>/appform.html', context)