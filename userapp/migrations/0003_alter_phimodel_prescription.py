# Generated by Django 4.0.4 on 2022-06-29 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_alter_phimodel_prescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phimodel',
            name='prescription',
            field=models.ImageField(null='True', upload_to='prescription/'),
        ),
    ]
