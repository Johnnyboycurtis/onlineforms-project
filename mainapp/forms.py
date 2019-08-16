from django.forms import ModelForm
from .models import Contacts, ProgrammingLanguages, Sports
from django.forms import modelformset_factory

class ContactsForm(ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'email', 'age']



class LanguagesForm(ModelForm):
    class Meta:
        model = ProgrammingLanguages
        fields = ['name', 'skill']



class SportsForm(ModelForm):
    class Meta:
        model = Sports
        fields = ['name', 'skill']



#LanguagesFormSet = modelformset_factory(ProgrammingLanguages, fields = ('name', 'skill'), extra = 5, max_num = 5)
#SportsFormSet = modelformset_factory(Sports, fields = ('name', 'skill'), extra = 5, max_num = 5)