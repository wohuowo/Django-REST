# Generated by Django 4.0.5 on 2022-06-30 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
