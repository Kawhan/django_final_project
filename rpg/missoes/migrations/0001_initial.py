# Generated by Django 4.1 on 2022-09-03 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='missoesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_missao', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('participantes', models.TextField()),
            ],
        ),
    ]
