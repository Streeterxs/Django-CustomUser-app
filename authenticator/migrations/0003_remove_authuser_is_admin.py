# Generated by Django 2.0.7 on 2018-08-02 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticator', '0002_auto_20180802_0114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authuser',
            name='is_admin',
        ),
    ]