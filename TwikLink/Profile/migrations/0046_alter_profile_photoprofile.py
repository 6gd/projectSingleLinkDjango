# Generated by Django 4.2.1 on 2023-10-19 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0045_alter_profile_photoprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photoProfile',
            field=models.CharField(blank=True, null=True),
        ),
    ]