# Generated by Django 2.1.7 on 2019-03-26 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecipesApp', '0004_auto_20190326_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(height_field='300', upload_to='', width_field='300'),
        ),
    ]
