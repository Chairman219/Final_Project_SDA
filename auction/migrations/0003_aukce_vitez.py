# Generated by Django 4.1 on 2024-09-30 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auction', '0002_profile_delete_uzivatel'),
    ]

    operations = [
        migrations.AddField(
            model_name='aukce',
            name='vitez',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vyhrane_aukce', to=settings.AUTH_USER_MODEL),
        ),
    ]
