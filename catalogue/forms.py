from django import forms
from catalogue.models import Catalogue

class CatalogueForm(forms.ModelForm):
    class Meta:
        model = Catalogue
        fields = "__all__"