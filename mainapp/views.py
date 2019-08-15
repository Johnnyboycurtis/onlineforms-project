from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ContactsForm, LanguagesFormSet, SportsFormSet
from django.contrib import messages

from .models import Contacts

def home(request):
    context = {'title': 'Home'}
    if request.method == "GET" and request.user.is_authenticated:
        print("print out the user's contacts now")
        context['contacts'] = Contacts.objects.all()
        return render(request, 'mainapp/home.html', context)

    return render(request, 'mainapp/home.html', context)

def about(request):
    context = {'title': 'About'}
    return render(request, 'mainapp/about.html', context)


@login_required
def createcontact(request):
    context = {'userinfoform': ContactsForm}
    if request.method == "POST":
        form = ContactsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit = False) # https://www.youtube.com/watch?v=2h57cqFRcqg
            instance.user = request.user
            instance.save()
            messages.success(request, "Saved new contact!")
            return redirect('home') #render(request, 'mainapp/home.html', {'form': form})
    return render(request, 'mainapp/createcontact.html', context)

@login_required
def detailedview(request, id):
    contact = Contacts.objects.get(pk = id)
    print(contact)
    return render(request, 'mainapp/detailedview.html', {'contact': contact})

