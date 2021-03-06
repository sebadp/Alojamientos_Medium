# Generated by Django 3.1.3 on 2021-01-19 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('category', models.CharField(choices=[('00', 'COMPARTIDA'), ('01', 'SIN AIRE ACONDICIONADO'), ('02', 'AIRE ACONDICIONADO'), ('03', 'FAMILIAR')], max_length=2)),
                ('beds', models.IntegerField()),
                ('capacity', models.IntegerField()),
            ],
        ),
    ]
