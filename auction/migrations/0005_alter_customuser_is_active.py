# Generated by Django 4.1 on 2024-09-26 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0004_remove_customuser_status_uctu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
