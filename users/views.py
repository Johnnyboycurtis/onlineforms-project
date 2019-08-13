from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            messages.success(request, "User {} created!".format(username))
            return redirect("home")
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)