# Generated by Django 4.2.1 on 2023-05-31 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0011_alter_profile_colordescription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='BackgroundProfile',
            field=models.ImageField(upload_to='BackgroundProfiles/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photoProfile',
            field=models.ImageField(upload_to='PhotoProfiles/'),
        ),
    ]
