# Generated by Django 2.2.3 on 2019-08-14 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('district', '0002_auto_20190813_0638'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction', models.TextField(blank=True, null=True)),
                ('sinhalaName', models.CharField(max_length=255, unique=True)),
                ('englishName', models.CharField(max_length=255, unique=True)),
                ('tamilName', models.CharField(max_length=255, unique=True)),
                ('area', models.CharField(blank=True, max_length=255, null=True)),
                ('featureImage', models.ImageField(blank=True, null=True, upload_to='images/city/')),
                ('mapUrl', models.URLField(blank=True, max_length=255, null=True, unique=True)),
                ('postal_code', models.IntegerField(unique=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='district.District')),
            ],
        ),
    ]
