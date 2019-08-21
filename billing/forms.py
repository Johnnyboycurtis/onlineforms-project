from django.forms import ModelForm, inlineformset_factory
from .models import BillHeader, BillLines


class BillHeaderForm(ModelForm):
    class Meta:
        model = BillHeader
        fields = ['company_name', 'street_address', 'city', 'state', 'phone', 'email']

BillLineFormSet = inlineformset_factory(BillHeader, BillLines, fields = ('description', 'quantity', 'unit_price'))