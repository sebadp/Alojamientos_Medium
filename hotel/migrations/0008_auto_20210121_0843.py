# Generated by Django 3.1.3 on 2021-01-21 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_auto_20210120_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='category',
            field=models.CharField(choices=[('CAB1', 'Saracura'), ('CAB2', 'Pa-caa')], max_length=6),
        ),
    ]