# Generated by Django 2.1.7 on 2019-03-31 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecipesApp', '0009_auto_20190329_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='count_views',
            field=models.IntegerField(default=0),
        ),
    ]