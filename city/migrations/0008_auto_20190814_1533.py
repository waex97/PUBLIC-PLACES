# Generated by Django 2.2.3 on 2019-08-14 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0007_auto_20190814_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='englishName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='sinhalaName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='tamilName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
