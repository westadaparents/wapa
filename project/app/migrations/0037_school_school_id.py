# Generated by Django 3.2.6 on 2021-08-20 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_isat'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='school_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
