# Generated by Django 4.0 on 2022-03-12 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imaging_database', '0016_spectralimage_alter_hospital_spectral_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tissue_class',
            name='classImage',
            field=models.ImageField(default=2, upload_to='classType/'),
            preserve_default=False,
        ),
    ]
