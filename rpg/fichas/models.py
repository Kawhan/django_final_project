from django.db import models
from jogadores.models import Jogador
from datetime import datetime


# Create your models here.
class fichaRpgModel(models.Model):
    jogador = models.ForeignKey(Jogador, on_delete=models.DO_NOTHING)
    nome_personagem = models.CharField(max_length=255)
    força = models.IntegerField()
    bonus_força = models.CharField(max_length=30)
    velocidade = models.IntegerField()
    bonus_velocidade = models.CharField(max_length=30)
    defesa = models.IntegerField()
    bonus_defesa = models.CharField(max_length=30)
    inteligencia = models.IntegerField()
    bonus_inteligencia = models.CharField(max_length=30)
    carisma = models.IntegerField()
    bonus_carisma = models.CharField(max_length=30)
    idade = models.IntegerField()
    historia = models.TextField()
    raça = models.CharField(max_length=100)
    classe = models.CharField(max_length=100)
    level = models.IntegerField()
    missoes = models.TextField()
    pontos_vida = models.IntegerField()
    pontos_mana = models.IntegerField()
    conquistas = models.TextField()
    is_dead = models.BooleanField(default=False)
    foto_personagem = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    
    def __str__(self):
        return self.nome_personagem
    
    class Meta:
        verbose_name = 'Ficha RPG'
        verbose_name_plural = 'Fichas RPG'