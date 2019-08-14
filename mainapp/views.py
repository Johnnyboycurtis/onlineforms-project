from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ContactsForm, LanguagesFormSet, SportsFormSet
from django.contrib import messages

def home(request):
    return render(request, 'mainapp/home.html')

def about(request):
    return render(request, 'mainapp/about.html')


@login_required
def newapp(request):
    context = {'userinfoform': ContactsForm}
    if request.method == "POST":
        form = ContactsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit = False) # https://www.youtube.com/watch?v=2h57cqFRcqg
            instance.user = request.user
            instance.save()
            messages.success(request, "Saved new contact!")
            return redirect('home') #render(request, 'mainapp/home.html', {'form': form})
    return render(request, 'mainapp/newapp.html', context)


def appform(request):
    return render(request, 'mainapp/home.html')

