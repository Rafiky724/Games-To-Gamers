# Generated by Django 4.2.16 on 2024-09-08 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JuegosApp', '0002_rename_games_game'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='categoria',
            new_name='plataforma',
        ),
    ]
