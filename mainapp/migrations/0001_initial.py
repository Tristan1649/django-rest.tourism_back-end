# Generated by Django 4.0.6 on 2022-07-12 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=344)),
                ('image', models.ImageField(blank=True, null=True, upload_to='event_img')),
                ('duration', models.CharField(max_length=344)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=233)),
                ('image', models.ImageField(upload_to='loc')),
                ('desc', models.TextField()),
                ('maps', models.URLField()),
                ('history', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('duration', models.CharField(max_length=344)),
                ('ocupation', models.IntegerField(verbose_name='множество')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.location')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=344)),
                ('image', models.ImageField(blank=True, null=True, upload_to='tur_gallery')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.location')),
            ],
        ),
    ]
