# Generated by Django 4.1.7 on 2023-02-24 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0013_alter_recipeingredient_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='amount',
            field=models.CharField(default='1', max_length=80, verbose_name='количество'),
        ),
    ]