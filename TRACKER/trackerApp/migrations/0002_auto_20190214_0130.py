# Generated by Django 2.1.7 on 2019-02-14 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackerApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
