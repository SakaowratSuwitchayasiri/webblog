# Generated by Django 3.2.11 on 2022-01-23 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_rename_post2_headgov'),
    ]

    operations = [
        migrations.DeleteModel(
            name='headGov',
        ),
    ]