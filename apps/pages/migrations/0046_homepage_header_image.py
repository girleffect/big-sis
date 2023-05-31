# Generated by Django 3.2.18 on 2023-04-11 02:46

from django.db import migrations
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0045_auto_20230411_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='header_image',
            field=wagtail.fields.StreamField([('Image', wagtail.images.blocks.ImageChooserBlock()), ('Document', wagtail.documents.blocks.DocumentChooserBlock())], blank=True, use_json_field=False),
        ),
    ]
