# Generated by Django 4.0 on 2022-01-20 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imaging_database', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hsi_feature',
            name='frames',
        ),
        migrations.RemoveField(
            model_name='hsi_feature',
            name='image',
        ),
        migrations.AddField(
            model_name='hsi_feature',
            name='img',
            field=models.ImageField(default=0, upload_to='hsi_images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hsi_feature',
            name='offer',
            field=models.BooleanField(default=False),
        ),
    ]
