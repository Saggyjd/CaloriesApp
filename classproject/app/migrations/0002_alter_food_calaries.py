# Generated by Django 5.0.2 on 2024-03-04 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='calaries',
            field=models.FloatField(),
        ),
    ]
