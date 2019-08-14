from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print("\nFORM IS VALID\n")
            username = form.cleaned_data.get("username")
            form.save()
            messages.success(request, "User {} created!".format(username))
            return redirect("home")
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    return render(request, 'users/profile.html')