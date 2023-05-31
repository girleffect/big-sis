# Generated by Django 3.2.18 on 2023-04-11 04:35

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20230411_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogindexpage',
            name='body',
            field=wagtail.fields.StreamField([('Social_Media_Posts_Section', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('subtitle', wagtail.blocks.TextBlock(required=False)), ('posts', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('link', wagtail.blocks.URLBlock(required=True))], required=False), required=False)), ('footnote', wagtail.blocks.CharBlock(required=False)), ('social_media_platforms', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(required=True)), ('link', wagtail.blocks.URLBlock(required=True))], required=False), required=False)), ('show_section', wagtail.blocks.BooleanBlock(label='Show/Hide Section', required=False))]))], blank=True, use_json_field=False),
        ),
    ]
