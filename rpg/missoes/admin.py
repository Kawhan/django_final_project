from django.contrib import admin
from .models import missoesModel

# Register your models here.



# Register your models here.
@admin.register(missoesModel)
class missoesAdmin(admin.ModelAdmin):
    list_display = ('nome_missao', 'description', "aberta")
    search_fields = ('nome_missao', 'description', "aberta")
    list_editable = ('aberta',)
    
    list_per_page = 5
    
    pass
    