# Generated by Django 3.2.18 on 2023-04-11 04:13

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('pages', '0046_homepage_header_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.fields.StreamField([('Columns_Section', wagtail.blocks.StructBlock([('columns', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('column', wagtail.blocks.StreamBlock([('paragraph', wagtail.blocks.StructBlock([('rich_text', wagtail.blocks.RichTextBlock())], required=False)), ('faq', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('question', wagtail.blocks.CharBlock(required=True)), ('answer', wagtail.blocks.TextBlock(required=True))], required=False), required=False))], required=False)), ('button', wagtail.blocks.StructBlock([('button_text', wagtail.blocks.CharBlock()), ('button_link', wagtail.blocks.URLBlock(required=False)), ('show_for', wagtail.blocks.ChoiceBlock(choices=[('desktop_mobile', 'Desktop/Mobile'), ('desktop', 'Desktop'), ('mobile', 'Mobile')], icon='cup'))], required=False)), ('grid', wagtail.blocks.StructBlock([('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.blocks.TextBlock())])))], required=False))])), ('width', wagtail.blocks.ChoiceBlock(choices=[('col-span-12', '100%'), ('col-span-7', '60%'), ('col-span-6', '50%'), ('col-span-5', '40%')], icon='cup'))])))]))], blank=True, use_json_field=False)),
                ('seo_image', models.ForeignKey(blank=True, help_text='The image displayed when a page gets posted on social media.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='pages.customimage', verbose_name='Seo Image')),
            ],
            options={
                'verbose_name': 'Content page',
            },
            bases=('wagtailcore.page',),
        ),
    ]
