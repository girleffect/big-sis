# Generated by Django 3.2.18 on 2023-09-08 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20230901_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='postpage',
            name='hit_counter',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
