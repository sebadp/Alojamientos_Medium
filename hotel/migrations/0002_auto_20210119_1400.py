# Generated by Django 3.1.3 on 2021-01-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('COMPARTIDA', 'COMPARTIDA'), ('SIN AIRE ACONDICIONADO', 'SIN AIRE ACONDICIONADO'), ('AIRE ACONDICIONADO', 'AIRE ACONDICIONADO'), ('FAMILIAR', 'FAMILIAR')], max_length=25),
        ),
    ]
