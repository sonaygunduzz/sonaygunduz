# Generated by Django 3.0.3 on 2020-05-22 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=150)),
                ('answer', models.TextField(max_length=200)),
                ('status', models.CharField(choices=[('True', 'Evet'), ('FALSE', 'HAYIR')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
