# Generated by Django 4.1 on 2024-10-09 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0012_rename_komentar_kupujiciho_hodnoceni_komentar_k_aukci_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='address',
            new_name='adress',
        ),
    ]
