# Generated by Django 3.0 on 2020-03-18 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='gambar',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='resep',
            name='gambar',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
