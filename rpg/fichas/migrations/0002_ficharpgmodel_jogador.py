# Generated by Django 4.1 on 2022-09-03 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jogadores', '0001_initial'),
        ('fichas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficharpgmodel',
            name='jogador',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='jogadores.jogador'),
            preserve_default=False,
        ),
    ]