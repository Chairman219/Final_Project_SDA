# Generated by Django 4.1 on 2024-10-16 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0018_remove_aukce_waiting_for_premium_confirmation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aukce',
            name='propagace',
        ),
    ]
