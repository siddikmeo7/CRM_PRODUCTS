# Generated by Django 5.0 on 2024-10-23 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
