# Generated by Django 3.2.18 on 2023-03-27 03:59

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0026_alter_homepage_body'),
        ('blog', '0003_postpage_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='body',
            field=wagtail.fields.StreamField([('Social_Media_Posts_Section', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('subtitle', wagtail.blocks.TextBlock(required=False)), ('posts', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('link', wagtail.blocks.URLBlock(required=True))], required=False), required=False)), ('footnote', wagtail.blocks.CharBlock(required=False)), ('social_media_platforms', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(required=True)), ('link', wagtail.blocks.URLBlock(required=True))], required=False), required=False))]))], blank=True, use_json_field=False),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='seo_image',
            field=models.ForeignKey(blank=True, help_text='The image displayed when a page gets posted on social media.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='pages.customimage', verbose_name='Seo Image'),
        ),
    ]
