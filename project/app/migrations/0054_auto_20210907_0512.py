# Generated by Django 3.2.7 on 2021-09-07 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0053_auto_20210906_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zone',
            name='trustee_email',
            field=models.EmailField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='zone',
            name='trustee_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]