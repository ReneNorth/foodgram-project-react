# Generated by Django 4.1.7 on 2023-02-22 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_rename_title_recipe_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='recipes/'),
        ),
    ]
