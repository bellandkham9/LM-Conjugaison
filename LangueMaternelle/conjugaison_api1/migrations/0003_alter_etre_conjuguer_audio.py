# Generated by Django 4.1.6 on 2023-02-14 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conjugaison_api1', '0002_etre_conjuguer_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etre_conjuguer',
            name='audio',
            field=models.FileField(blank=True, upload_to='Documents/'),
        ),
    ]