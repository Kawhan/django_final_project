from django.contrib import admin
from .models import Jogador

# Register your models here.
@admin.register(Jogador)
class FichaRpgAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'email')
    search_fields = ('id','nome', 'email')
    
    list_per_page = 10
    
    pass
