# Generated by Django 3.0.4 on 2020-03-31 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todolist',
            new_name='Task',
        ),
    ]