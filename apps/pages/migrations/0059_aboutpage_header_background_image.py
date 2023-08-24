# Generated by Django 3.2.18 on 2023-08-23 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0058_auto_20230823_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='header_background_image',
            field=models.ForeignKey(blank=True, help_text='Recommended aspect ratio: 16/9 and image dimensions: 1920x1080', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='pages.customimage', verbose_name='Header background image'),
        ),
    ]