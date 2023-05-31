from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class SocialMediaPostBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True,help_text = 'Recommended aspect ratio: 2/3 and image dimensions: 240x360')
    youtube_video_id = blocks.CharBlock(required=True)
    class Meta:
        icon = ''


class SocialMediaPlatformBlock(blocks.StructBlock):
    icon = ImageChooserBlock(required=True)
    link = blocks.URLBlock(required=True)
    class Meta:
        icon = ''

class SocialMediaPostsBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    subtitle = blocks.TextBlock(required=False)
    posts = blocks.ListBlock(SocialMediaPostBlock(required=False), required=False)
    footnote = blocks.CharBlock(required=False)
    social_media_platforms = blocks.ListBlock(SocialMediaPlatformBlock(required=False), required=False)
    hide_section = blocks.BooleanBlock(required=False,label='Hide Section')
    hide_on_moya = blocks.BooleanBlock(required=False,label='Hide Section on Moya App')

    class Meta:
        template = 'blog/blocks/social-media-posts-block.html'
        icon = ''

