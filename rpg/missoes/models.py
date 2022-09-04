from django.db import models

# Create your models here.

class missoesModel(models.Model):
    nome_missao = models.CharField(max_length=255)
    description = models.TextField()
    participantes = models.TextField()
    foto_missao = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    aberta = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.nome_missao
            
    class Meta:
        verbose_name = 'Missão do RPG'
        verbose_name_plural = 'Missões RPG'