# Generated by Django 3.2.25 on 2024-08-03 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_rename_voetbalspelers_voetbalspeler'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voetbalspeler',
            name='auteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
