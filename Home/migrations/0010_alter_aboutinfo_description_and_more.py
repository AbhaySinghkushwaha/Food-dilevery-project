# Generated by Django 4.0.3 on 2022-09-19 11:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_rename_name_aboutinfo_title_remove_aboutinfo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutinfo',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurantinfo',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
