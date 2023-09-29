# Generated by Django 4.2.1 on 2023-05-31 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0013_profile_gradientactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='verifyUser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gradientoption',
            field=models.CharField(blank=True, choices=[('to top', 'Top'), ('to right top', 'Right top'), ('to right', 'Right'), ('to right bottom', 'Right bottom'), ('to bottom', 'Bottom'), ('to left bottom', 'Left bottom'), ('to left', 'Left'), ('to left top', 'Left top')], max_length=30, null=True),
        ),
    ]
