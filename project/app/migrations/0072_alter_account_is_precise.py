# Generated by Django 3.2.8 on 2021-10-21 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0071_auto_20211021_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_precise',
            field=models.BooleanField(null=True),
        ),
    ]
