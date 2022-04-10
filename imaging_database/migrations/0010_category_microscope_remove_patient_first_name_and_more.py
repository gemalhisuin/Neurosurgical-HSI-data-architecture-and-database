# Generated by Django 4.0 on 2022-02-25 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imaging_database', '0009_alter_mask_mask_alter_rgb_rgb_hs_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Microscope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Microscope/')),
            ],
        ),
        migrations.RemoveField(
            model_name='patient',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='last_name',
        ),
        migrations.AddField(
            model_name='hs_image',
            name='date_created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hs_image',
            name='last_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hs_image',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='hs_image',
            name='uniqueId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='rgb',
            name='date_created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rgb',
            name='last_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rgb',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='rgb',
            name='uniqueId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='diagnosis_history',
            name='patient',
            field=models.ManyToManyField(blank=True, to='imaging_database.Patient'),
        ),
        migrations.DeleteModel(
            name='Date_time',
        ),
        migrations.AddField(
            model_name='hs_image',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imaging_database.category'),
        ),
        migrations.AddField(
            model_name='rgb',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imaging_database.category'),
        ),
    ]
