from django import forms
from .models import fichaRpgModel

class fichaRpgForm(forms.ModelForm):
    class Meta:
        model = fichaRpgModel
        
        fields = [
            "nome_personagem",
            "força",
            "bonus_força",
            "velocidade",
            "bonus_velocidade",
            "defesa",
            "bonus_defesa",
            "inteligencia",
            "bonus_inteligencia",
            "carisma",
            "bonus_carisma",
            "idade",
            "historia",
            "raça",
            "classe",
            "level",
            "missoes",
            "pontos_vida",
            "pontos_mana",
            "conquistas",
            "jogador",
            'foto_personagem'
        ]