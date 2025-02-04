# Generated by Django 5.0.6 on 2024-07-05 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country_range',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Servicetype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='umra_pict/')),
                ('phone_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Availibilties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('duration', models.DurationField()),
                ('meal', models.CharField(max_length=50)),
                ('medical_care', models.CharField(max_length=20)),
                ('guidelines', models.CharField(max_length=10)),
                ('provided_appliances', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availabilities', to='blog.country_range')),
                ('servicetype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availabilities', to='blog.servicetype')),
            ],
        ),
    ]
