# Generated by Django 4.2.1 on 2023-06-01 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0024_alter_profile_gradientone_alter_profile_gradienttwo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photoProfile',
            field=models.ImageField(blank=True, default='asstes/images/806c33e6481b79ba7ec27073f24cb781.jpg', null=True, upload_to='PhotoProfiles/'),
        ),
    ]
