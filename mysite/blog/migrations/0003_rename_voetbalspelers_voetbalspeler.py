# Generated by Django 3.2.25 on 2024-08-03 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_voetbalspelers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Voetbalspelers',
            new_name='Voetbalspeler',
        ),
    ]
