# Generated by Django 3.2.18 on 2023-08-23 08:09

from django.db import migrations
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0057_auto_20230823_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='header_image',
            field=wagtail.fields.StreamField([('Image', wagtail.images.blocks.ImageChooserBlock(help_text='Recommended aspect ratio: 1/1 and minimum width 900px')), ('Document', wagtail.documents.blocks.DocumentChooserBlock())], blank=True, use_json_field=False, verbose_name='Header right side image'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='header_left_side_image',
            field=wagtail.fields.StreamField([('Image', wagtail.images.blocks.ImageChooserBlock(help_text='Recommended aspect ratio: 16/9 and minimum width 900px')), ('Document', wagtail.documents.blocks.DocumentChooserBlock())], blank=True, use_json_field=False, verbose_name='Header left side image'),
        ),
    ]
