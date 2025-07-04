# Generated by Django 5.1.6 on 2025-03-05 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cafe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('address', models.TextField()),
                ('opening_hours', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('menu', models.TextField()),
                ('services', models.JSONField()),
                ('social_media', models.JSONField()),
            ],
        ),
    ]
