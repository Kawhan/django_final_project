from django import forms
from .models import missoesModel

class MissoesForm(forms.ModelForm):
    class Meta:
        model = missoesModel
        
        fields = [
            "nome_missao",
            "description",
            "participantes",
            "foto_missao",
            "aberta",
        ]