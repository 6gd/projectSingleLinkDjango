# Generated by Django 4.2.1 on 2023-05-30 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0010_remove_profile_id_alter_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='colorDescription',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='colorUser',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gradientOne',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gradientTwo',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
