# Generated by Django 4.0 on 2022-02-25 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imaging_database', '0011_rgb_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='rgb',
            name='gray',
            field=models.ImageField(default=1, upload_to='gray/'),
            preserve_default=False,
        ),
    ]
