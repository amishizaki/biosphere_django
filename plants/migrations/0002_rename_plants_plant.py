# Generated by Django 4.1 on 2022-11-18 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Plants',
            new_name='Plant',
        ),
    ]
