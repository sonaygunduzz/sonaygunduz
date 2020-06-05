# Generated by Django 3.0.3 on 2020-06-05 10:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_reservation_reservationvehicle'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationvehicle',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservationvehicle',
            name='kalkisyeri',
            field=models.CharField(blank=True, max_length=255, verbose_name='Kalkış Yeri'),
        ),
        migrations.AddField(
            model_name='reservationvehicle',
            name='varisyeri',
            field=models.CharField(blank=True, max_length=255, verbose_name='Varış Yeri'),
        ),
    ]