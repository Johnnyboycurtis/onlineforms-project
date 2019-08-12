from django.forms import ModelForm
from .models import UserInfo, ProgrammingLanguages, Sports
from django.forms import formset_factory

class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ['name', 'email', 'age']



class LanguagesForm(ModelForm):
    class Meta:
        model = ProgrammingLanguages
        fields = ['name', 'skill']



class SportsForm(ModelForm):
    class Meta:
        model = Sports
        fields = ['name', 'skill']



LanguagesFormSet = formset_factory(LanguagesForm, extra = 1)
SportsFormSet = formset_factory(SportsForm, extra = 1)