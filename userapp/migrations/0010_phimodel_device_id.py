# Generated by Django 4.0.4 on 2022-07-02 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0009_phimodel_device_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='phimodel',
            name='device_id',
            field=models.IntegerField(null=True),
        ),
    ]
