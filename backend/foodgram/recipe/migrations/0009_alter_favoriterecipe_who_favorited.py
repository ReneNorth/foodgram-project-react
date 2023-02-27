# Generated by Django 4.1.7 on 2023-02-23 08:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0008_alter_favoriterecipe_favorited_recipe_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoriterecipe',
            name='who_favorited',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='who_favorited', to=settings.AUTH_USER_MODEL),
        ),
    ]
