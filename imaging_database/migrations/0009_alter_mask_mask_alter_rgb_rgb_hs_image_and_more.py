# Generated by Django 4.0 on 2022-02-09 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imaging_database', '0008_remove_hospital_spectral_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mask',
            name='mask',
            field=models.ImageField(upload_to='mask/'),
        ),
        migrations.AlterField(
            model_name='rgb',
            name='rgb',
            field=models.ImageField(upload_to='RGB/'),
        ),
        migrations.CreateModel(
            name='HS_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hs_image', models.ImageField(upload_to='hsi_images/')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imaging_database.patient')),
            ],
        ),
        migrations.AddField(
            model_name='hospital',
            name='spectral_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imaging_database.hs_image'),
        ),
        migrations.AddField(
            model_name='imaging',
            name='spectral_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imaging_database.hs_image'),
        ),
        migrations.AddField(
            model_name='mask',
            name='spectral_image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imaging_database.hs_image'),
        ),
        migrations.AddField(
            model_name='metadata',
            name='spectral_image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imaging_database.hs_image'),
        ),
        migrations.AddField(
            model_name='rgb',
            name='spectral_image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imaging_database.hs_image'),
        ),
    ]
