from django.forms import ModelForm, inlineformset_factory, Textarea
from .models import BillHeader, BillLines


class BillHeaderForm(ModelForm):
    class Meta:
        model = BillHeader
        fields = ['company_name', 'street_address', 'city', 'state', 'phone', 'email']


class BillLineForm(ModelForm):
    class Meta:
        model = BillLines
        fields = ('description', 'quantity', 'unit_price')
        widgets = {
          "description": Textarea(attrs={'rows':2, 'cols':20}),
        }


BillLineFormSet = inlineformset_factory(BillHeader, BillLines, fields = ('description', 'quantity', 'unit_price'), form = BillLineForm)
