# Generated by Django 4.1.4 on 2022-12-08 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_images_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.CharField(max_length=70, verbose_name='paso')),
                ('status', models.CharField(max_length=50, verbose_name='estado')),
                ('star_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.images')),
            ],
        ),
    ]
