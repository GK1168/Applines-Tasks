# Generated by Django 4.2.2 on 2023-06-09 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApp', '0002_examdetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examdetails',
            old_name='Percentage',
            new_name='percentage',
        ),
    ]
