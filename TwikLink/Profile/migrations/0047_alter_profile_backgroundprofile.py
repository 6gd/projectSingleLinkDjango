# Generated by Django 4.2.1 on 2023-11-14 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0046_alter_profile_photoprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='BackgroundProfile',
            field=models.CharField(blank=True, null=True),
        ),
    ]
