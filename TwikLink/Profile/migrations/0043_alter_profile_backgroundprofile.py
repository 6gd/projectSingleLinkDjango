# Generated by Django 4.2.1 on 2023-09-13 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0042_alter_item_backgroundbox'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='BackgroundProfile',
            field=models.ImageField(blank=True, default='/asstes/images/backgroundProfile.jpg', null=True, upload_to='BackgroundProfiles/'),
        ),
    ]
