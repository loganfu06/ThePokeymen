# Generated by Django 4.2 on 2024-01-12 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0003_alter_pokemon_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
