# Generated by Django 3.2.7 on 2021-09-21 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voterapi', '0002_auto_20210921_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='address',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='voter',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='voter',
            name='place',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
