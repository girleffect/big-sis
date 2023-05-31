# Generated by Django 3.2.18 on 2023-03-24 08:46

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_rename_facebook_link_homepage_messenger_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('Featured_Blog_Post_Section', wagtail.blocks.StructBlock([('featured_blog_post', wagtail.blocks.PageChooserBlock(help_text='If empty the latest blog post will be displayed.', page_type=['blog.PostPage'], required=False))])), ('About_Section', wagtail.blocks.StructBlock([])), ('Social_Media_Posts_Section', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('subtitle', wagtail.blocks.TextBlock(required=False)), ('posts', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('link', wagtail.blocks.URLBlock(required=True))], required=False), required=False)), ('footnote', wagtail.blocks.CharBlock(required=False)), ('social_media_platforms', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(required=True)), ('link', wagtail.blocks.URLBlock(required=True))], required=False), required=False))])), ('Latest_Blog_Posts_Section', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('number_of_posts_to_show', wagtail.blocks.IntegerBlock(default=4))]))], blank=True, use_json_field=None),
        ),
    ]
