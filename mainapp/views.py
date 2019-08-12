from django.shortcuts import render
from .forms import UserInfoForm, LanguagesFormSet, SportsFormSet

def home(request):
    return render(request, 'mainapp/home.html')

def newapp(request):
    context = {'userinfoform': UserInfoForm}
    #print(dir(request))
    print(request.method)
    if request.method == "POST":
        print(request.POST)
        form = UserInfoForm(request.POST)
        print(form)
        if form.is_valid():
            print("form is valid")
            return render(request, 'mainapp/home.html', {'form': form})
    return render(request, 'mainapp/newapp.html', context)


def appform(request, userid):
    context = {'userinfoform': UserInfoForm, 'languagesform': LanguagesFormSet, 'sportsform': SportsFormSet}
    return render(request, 'mainapp/<userid>/appform.html', context)

"""
def edit_appform(request, userid):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
"""