# Generated by Django 4.2.1 on 2023-05-30 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0005_alter_username_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='username',
            old_name='slug',
            new_name='Allinfo',
        ),
    ]
