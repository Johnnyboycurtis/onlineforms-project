from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ContactsForm
from django.contrib import messages
from django.forms import inlineformset_factory
from .models import Contacts, ProgrammingLanguages, Sports

def home(request):
    context = {'title': 'Home'}
    if request.method == "GET" and request.user.is_authenticated:
        #print("print out the user's contacts now")
        context['contacts'] = Contacts.objects.filter(user_id = request.user.id)
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
    #print(dir(contact))
    return render(request, 'mainapp/detailedview.html', {'contact': contact})

@login_required
def editview(request, id):
    contact = Contacts.objects.get(pk = id)
    LanguagesFormSet = inlineformset_factory(Contacts, ProgrammingLanguages, fields = ('name', 'skill'))

    if request.method == "POST":
        formset = LanguagesFormSet(request.POST, instance = contact)
        formset.contact = contact
        if formset.is_valid():
            formset.save()
            messages.success(request, "Saved new information")
            return redirect('editview', id=id)

    formset = LanguagesFormSet(instance = contact)
    context = {'formset': formset, 'title': 'Edit View'}
    return render(request, 'mainapp/editview.html', context)
