# Generated by Django 3.2.18 on 2023-09-07 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0061_auto_20230904_0529'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='header_background_color_hex_code',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
