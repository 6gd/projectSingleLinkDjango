# Generated by Django 4.2.1 on 2023-06-13 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0026_remove_profile_coloruser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photoProfile',
            field=models.ImageField(blank=True, null=True, upload_to='PhotoProfiles/'),
        ),
    ]
