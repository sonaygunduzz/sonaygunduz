# Generated by Django 3.0.3 on 2020-05-22 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200522_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='reservationnumber',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
