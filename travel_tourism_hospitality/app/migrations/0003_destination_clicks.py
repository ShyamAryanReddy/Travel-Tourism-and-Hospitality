# Generated by Django 4.1.3 on 2022-12-04 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_userdestinations_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='clicks',
            field=models.IntegerField(default=0),
        ),
    ]