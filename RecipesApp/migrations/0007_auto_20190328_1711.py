# Generated by Django 2.1.7 on 2019-03-28 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecipesApp', '0006_auto_20190326_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='text',
            field=models.TextField(max_length=2000),
        ),
    ]
