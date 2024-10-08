# Generated by Django 3.2.18 on 2024-10-08 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpers', '0010_globalsettings_ga_measurement_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalsettings',
            name='external_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='globalsettings',
            name='external_url_text',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
