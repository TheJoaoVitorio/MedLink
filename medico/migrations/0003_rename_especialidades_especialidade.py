# Generated by Django 5.0.4 on 2024-04-21 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0002_dadosmedico'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Especialidades',
            new_name='Especialidade',
        ),
    ]
