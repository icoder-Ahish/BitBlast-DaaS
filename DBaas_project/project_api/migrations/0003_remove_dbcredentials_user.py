# Generated by Django 4.2.7 on 2023-11-21 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_api', '0002_dbcredentials'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dbcredentials',
            name='user',
        ),
    ]