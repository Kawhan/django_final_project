# Generated by Django 4.1 on 2022-09-03 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fichaRpgModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_personagem', models.CharField(max_length=255)),
                ('força', models.IntegerField()),
                ('bonus_força', models.CharField(max_length=30)),
                ('velocidade', models.IntegerField()),
                ('bonus_velocidade', models.CharField(max_length=30)),
                ('defesa', models.IntegerField()),
                ('bonus_defesa', models.CharField(max_length=30)),
                ('inteligencia', models.IntegerField()),
                ('bonus_inteligencia', models.CharField(max_length=30)),
                ('carisma', models.IntegerField()),
                ('bonus_carisma', models.CharField(max_length=30)),
                ('idade', models.IntegerField()),
                ('historia', models.TextField()),
                ('raça', models.CharField(max_length=100)),
                ('classe', models.CharField(max_length=100)),
                ('level', models.IntegerField()),
                ('missoes', models.TextField()),
                ('pontos_vida', models.IntegerField()),
                ('pontos_mana', models.IntegerField()),
                ('conquistas', models.TextField()),
            ],
            options={
                'verbose_name': 'Ficha RPG',
                'verbose_name_plural': 'Fichas RPG',
            },
        ),
    ]
