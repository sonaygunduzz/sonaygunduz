# Generated by Django 3.0.3 on 2020-04-10 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0005_auto_20200409_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='slug',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='keywords',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
