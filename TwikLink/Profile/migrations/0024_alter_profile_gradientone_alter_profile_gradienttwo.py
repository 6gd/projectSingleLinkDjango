# Generated by Django 4.2.1 on 2023-06-01 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0023_alter_profile_photoprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gradientOne',
            field=models.CharField(blank=True, default='#5558da', max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gradientTwo',
            field=models.CharField(blank=True, default='#5fd1f9', max_length=7, null=True),
        ),
    ]
