# Generated by Django 3.2.7 on 2021-09-29 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_auto_20210929_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='datetime',
            field=models.DateField(blank=True, null=True),
        ),
    ]
