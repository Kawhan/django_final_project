from django.contrib import admin
from .models import fichaRpgModel

# Register your models here.
@admin.register(fichaRpgModel)
class FichaRpgAdmin(admin.ModelAdmin):
    list_display = ('nome_personagem', 'idade', 'level', 'raça', 'classe','is_dead')
    search_fields = ('nome_personagem', 'raça', 'classe')
    list_editable = ('is_dead',)
    
    list_per_page = 5
    
    pass
    