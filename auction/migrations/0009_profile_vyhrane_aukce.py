# Generated by Django 4.1 on 2024-10-03 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0008_aukce_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='vyhrane_aukce',
            field=models.ManyToManyField(blank=True, related_name='vyhrane_aukce', to='auction.aukce'),
        ),
    ]
