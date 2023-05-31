# Generated by Django 3.2.18 on 2023-05-09 08:04

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0053_auto_20230509_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='body',
            field=wagtail.fields.StreamField([('Time_Line_Section', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('year', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.TextBlock())], required=False), required=False)), ('hide_section', wagtail.blocks.BooleanBlock(label='Hide Section', required=False)), ('hide_on_moya', wagtail.blocks.BooleanBlock(label='Hide Section on Moya App', required=False))])), ('Key_Figures_And_Testimonials_Section', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('key_figures', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('numbers', wagtail.blocks.CharBlock(required=False)), ('description', wagtail.blocks.CharBlock(required=False))], required=False), required=False)), ('testimonials', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('description', wagtail.blocks.TextBlock())], required=False), required=False)), ('hide_section', wagtail.blocks.BooleanBlock(label='Hide Section', required=False)), ('hide_on_moya', wagtail.blocks.BooleanBlock(label='Hide Section on Moya App', required=False))])), ('Faq_Section', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('question', wagtail.blocks.CharBlock(required=True)), ('answer', wagtail.blocks.TextBlock(required=True))], required=False), required=False)), ('hide_section', wagtail.blocks.BooleanBlock(label='Hide Section', required=False)), ('hide_on_moya', wagtail.blocks.BooleanBlock(label='Hide Section on Moya App', required=False))]))], blank=True, use_json_field=False),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='body',
            field=wagtail.fields.StreamField([('Columns_Section', wagtail.blocks.StructBlock([('columns', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('column', wagtail.blocks.StreamBlock([('paragraph', wagtail.blocks.StructBlock([('rich_text', wagtail.blocks.RichTextBlock())], required=False)), ('faq', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('question', wagtail.blocks.CharBlock(required=True)), ('answer', wagtail.blocks.TextBlock(required=True))], required=False), required=False))], required=False)), ('button', wagtail.blocks.StructBlock([('button_text', wagtail.blocks.CharBlock()), ('button_link', wagtail.blocks.URLBlock(required=False)), ('show_for', wagtail.blocks.ChoiceBlock(choices=[('desktop_mobile', 'Desktop/Mobile'), ('desktop', 'Desktop'), ('mobile', 'Mobile')], icon='cup'))], required=False)), ('grid', wagtail.blocks.StructBlock([('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Recommended aspect ratio: 1/1 and image dimensions: 250x250')), ('text', wagtail.blocks.TextBlock())])))], required=False))])), ('width', wagtail.blocks.ChoiceBlock(choices=[('col-span-12', '100%'), ('col-span-7', '60%'), ('col-span-6', '50%'), ('col-span-5', '40%')], icon='cup'))]))), ('hide_section', wagtail.blocks.BooleanBlock(label='Hide Section', required=False)), ('hide_on_moya', wagtail.blocks.BooleanBlock(label='Hide Section on Moya App', required=False))]))], blank=True, use_json_field=False),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('Featured_Blog_Post_Section', wagtail.blocks.StructBlock([('featured_blog_post', wagtail.blocks.PageChooserBlock(help_text='If empty the latest blog post will be displayed.', page_type=['blog.PostPage'], required=False)), ('hide_section', wagtail.blocks.BooleanBlock(label='Hide Section', required=False)), ('hide_on_moya', wagtail.blocks.BooleanBlock(label='Hide Section on Moya App', required=False))])), ('Columns_Section', wagtail.blocks.StructBlock([('columns', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('column', wagtail.blocks.StreamBlock([('paragraph', wagtail.blocks.StructBlock([('rich_text', wagtail.blocks.RichTextBlock())], required=False)), ('faq', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('question', wagtail.blocks.CharBlock(required=True)), ('answer', wagtail.blocks.TextBlock(required=True))], required=False), required=False))], required=False)), ('button', wagtail.blocks.StructBlock([('button_text', wagtail.blocks.CharBlock()), ('button_link', wagtail.blocks.URLBlock(required=False)), ('show_for', wagtail.blocks.ChoiceBlock(choices=[('desktop_mobile', 'Desktop/Mobile'), ('desktop', 'Desktop'), ('mobile', 'Mobile')], icon='cup'))], required=False)), ('grid', wagtail.blocks.StructBlock([('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Recommended aspect ratio: 1/1 and image dimensions: 250x250')), ('text', wagtail.blocks.TextBlock())])))], required=False))])), ('width', wagtail.blocks.ChoiceBlock(choices=[('col-span-12', '100%'), ('col-span-7', '60%'), ('col-span-6', '50%'), ('col-span-5', '40%')], icon='cup'))]))), ('hide_section', wagtail.blocks.BooleanBlock(label='Hide Section', required=False)), ('hide_on_moya', wagtail.blocks.BooleanBlock(label='Hide Section on Moya App', required=False))])), ('Social_Media_Posts_Section', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('subtitle', wagtail.blocks.TextBlock(required=False)), ('posts', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Recommended aspect ratio: 2/3 and image dimensions: 600x900', required=True)), ('link', wagtail.blocks.URLBlock(required=True))], required=False), required=False)), ('footnote', wagtail.blocks.CharBlock(required=False)), ('social_media_platforms', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(required=True)), ('link', wagtail.blocks.URLBlock(required=True))], required=False), required=False)), ('hide_section', wagtail.blocks.BooleanBlock(label='Hide Section', required=False)), ('hide_on_moya', wagtail.blocks.BooleanBlock(label='Hide Section on Moya App', required=False))])), ('Latest_Blog_Posts_Section', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('number_of_posts_to_show', wagtail.blocks.IntegerBlock(default=4)), ('hide_section', wagtail.blocks.BooleanBlock(label='Hide Section', required=False)), ('hide_on_moya', wagtail.blocks.BooleanBlock(label='Hide Section on Moya App', required=False))]))], blank=True, use_json_field=False),
        ),
    ]
