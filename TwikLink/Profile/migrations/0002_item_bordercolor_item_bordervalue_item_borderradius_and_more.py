# Generated by Django 4.2.1 on 2023-11-21 16:41

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='BorderColor',
            field=colorfield.fields.ColorField(blank=True, default='#000000', image_field=None, max_length=25, null=True, samples=None),
        ),
        migrations.AddField(
            model_name='item',
            name='BorderValue',
            field=models.IntegerField(blank=True, default=2, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='Borderradius',
            field=models.IntegerField(blank=True, default=6, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='backgroundbox',
            field=colorfield.fields.ColorField(blank=True, default='#7a7a7a', image_field=None, max_length=25, null=True, samples=None),
        ),
        migrations.AlterField(
            model_name='item',
            name='gradientOne',
            field=colorfield.fields.ColorField(blank=True, default='#5558da', image_field=None, max_length=25, null=True, samples=None),
        ),
        migrations.AlterField(
            model_name='item',
            name='gradientTwo',
            field=colorfield.fields.ColorField(blank=True, default='#5fd1f9', image_field=None, max_length=25, null=True, samples=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='colorDescription',
            field=colorfield.fields.ColorField(blank=True, default='#ffffff', image_field=None, max_length=25, null=True, samples=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gradientOne',
            field=colorfield.fields.ColorField(blank=True, default='#ffffff', image_field=None, max_length=25, null=True, samples=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gradientTwo',
            field=colorfield.fields.ColorField(blank=True, default='#4dffff', image_field=None, max_length=25, null=True, samples=None),
        ),
    ]
