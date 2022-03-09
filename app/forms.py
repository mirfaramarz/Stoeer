from django import forms
from .models import BankData

class BankDataForm(forms.ModelForm):
    class Meta:
        model = BankData
        exclude = ("owner", )