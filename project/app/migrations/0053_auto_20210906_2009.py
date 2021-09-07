# Generated by Django 3.2.7 on 2021-09-07 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0052_voter_address_json'),
    ]

    operations = [
        migrations.AddField(
            model_name='zone',
            name='trustee_email',
            field=models.EmailField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='zone',
            name='trustee_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]