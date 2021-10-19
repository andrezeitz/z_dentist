# Generated by Django 3.2.7 on 2021-10-19 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_alter_appointment_treatment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='treatment',
            field=models.CharField(choices=[('Basic dentist Survey: 100€', 'BASIC DENTIST SURVEY: 100€'), ('Teeth whitening Service: 300€', 'TEETH WHITENING SERVICE: 300€'), ('Ceramic crowns and fillings: 100€', 'CERAMIC CROWNS AND FILLINGS: 100€'), ('Remove crowns, bridges Service: 50€', 'REMOVE CROWNS, BRIDGES SERVICE: 50€'), ('Overlay teeth whitening: 170€', 'OVERLAY TEETH WHITENING: 170€'), ('Make Braces: 2400€', 'MAKE BRACES: 2400€'), ('Covering the recession of the gums: 400€', 'COVERING THE RECESSION OF THE GUMS: 400€'), ('Removal of tooth: 150€', 'REMOVAL OF TOOTH: 150€'), ('Removal of tartar: 50€', 'REMOVAL OF TARTAR: 50€')], default='Basic dentist survey: 100€', max_length=100),
        ),
    ]
