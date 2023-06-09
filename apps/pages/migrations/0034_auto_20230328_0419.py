# Generated by Django 3.2.18 on 2023-03-28 04:19

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0033_auto_20230328_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privacypolicypage',
            name='body',
            field=wagtail.fields.StreamField([('Columns_Section', wagtail.blocks.StructBlock([('columns', wagtail.blocks.StreamBlock([('column', wagtail.blocks.StreamBlock([('paragraph', wagtail.blocks.StructBlock([('rich_text', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image']))], required=False)), ('faq', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('question', wagtail.blocks.CharBlock(required=True)), ('answer', wagtail.blocks.TextBlock(required=True))], required=False), required=False))], required=False)), ('button', wagtail.blocks.StructBlock([], required=False)), ('grid', wagtail.blocks.StructBlock([], required=False))]))])), ('width', wagtail.blocks.ChoiceBlock(choices=[('col-span-12', '100%'), ('col-span-7', '60%'), ('col-span-6', '50%'), ('col-span-5', '40%')], icon='cup'))]))], blank=True, use_json_field=False),
        ),
        migrations.AlterField(
            model_name='termsandconditionspage',
            name='body',
            field=wagtail.fields.StreamField([('Columns_Section', wagtail.blocks.StructBlock([('columns', wagtail.blocks.StreamBlock([('column', wagtail.blocks.StreamBlock([('paragraph', wagtail.blocks.StructBlock([('rich_text', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image']))], required=False)), ('faq', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('question', wagtail.blocks.CharBlock(required=True)), ('answer', wagtail.blocks.TextBlock(required=True))], required=False), required=False))], required=False)), ('button', wagtail.blocks.StructBlock([], required=False)), ('grid', wagtail.blocks.StructBlock([], required=False))]))])), ('width', wagtail.blocks.ChoiceBlock(choices=[('col-span-12', '100%'), ('col-span-7', '60%'), ('col-span-6', '50%'), ('col-span-5', '40%')], icon='cup'))]))], blank=True, use_json_field=False),
        ),
    ]
