# Generated by Django 3.2.18 on 2023-03-24 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_alter_homepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='facebook_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='moya_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='whatsapp_link',
            field=models.URLField(blank=True),
        ),
    ]
