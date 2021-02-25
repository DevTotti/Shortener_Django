from django import forms
from .models import Mainurl


class UrlForm(forms.ModelForm):
    class Meta:
        model = Mainurl
        fields = ['original_url']

        widgets = {
            "original_url": forms.TextInput(attrs = {"class":"search", "placeholder":"Shorten your url", "autocomplete":"off"})
        }