from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

### About page blocks
class FaqItemBlock(blocks.StructBlock):
    question = blocks.CharBlock(required=True)
    answer = blocks.TextBlock(required=True)

    class Meta:
        icon = ''


class FaqBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    items = blocks.ListBlock(FaqItemBlock(required=False), required=False)
    hide_section = blocks.BooleanBlock(required=False,label='Hide Section')
    hide_on_moya = blocks.BooleanBlock(required=False,label='Hide Section on Moya App')
    
    class Meta:
        template = 'pages/blocks/about_page/faq-block.html'
        icon = ''

class TimeLineItemBlock(blocks.StructBlock):
    year = blocks.CharBlock()
    description = blocks.TextBlock()

    class Meta:
        icon = ''


class TimeLineBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    items = blocks.ListBlock(TimeLineItemBlock(required=False), required=False)
    hide_section = blocks.BooleanBlock(required=False,label='Hide Section')
    hide_on_moya = blocks.BooleanBlock(required=False,label='Hide Section on Moya App')

    class Meta:
        template = 'pages/blocks/about_page/time-line-block.html'
        icon = ''


class KeyFigureBlock(blocks.StructBlock):
    numbers = blocks.CharBlock(required=False)
    description = blocks.CharBlock(required=False)

    class Meta:
        icon = ''


class TestimonialBlock(blocks.StructBlock):
    name = blocks.CharBlock(required=False)
    photo = ImageChooserBlock(required=False)
    description = blocks.TextBlock()

    class Meta:
        icon = ''


class KeyFiguresAndTestimonialsBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    key_figures = blocks.ListBlock(KeyFigureBlock(required=False), required=False)
    testimonials = blocks.ListBlock(TestimonialBlock(required=False), required=False)
    hide_section = blocks.BooleanBlock(required=False,label='Hide Section')
    hide_on_moya = blocks.BooleanBlock(required=False,label='Hide Section on Moya App')

    class Meta:
        template = 'pages/blocks/about_page/key-figures-and-testimonials-block.html'
        icon = ''


### Home page blocks
class FeaturedBlogPostBlock(blocks.StructBlock):
    featured_blog_post = blocks.PageChooserBlock(required=False, target_model='blog.PostPage',
                                                 help_text='If empty the latest blog post will be displayed.')
    hide_section = blocks.BooleanBlock(required=False,label='Hide Section')
    hide_on_moya = blocks.BooleanBlock(required=False,label='Hide Section on Moya App')

    class Meta:
        template = 'pages/blocks/home_page/featured-blog-post-block.html'
        icon = ''


class LatestBlogPostsBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    number_of_posts_to_show = blocks.IntegerBlock(default=4)
    hide_section = blocks.BooleanBlock(required=False,label='Hide Section')
    hide_on_moya = blocks.BooleanBlock(required=False,label='Hide Section on Moya App')

    class Meta:
        template = 'pages/blocks/home_page/latest-blog-posts-block.html'
        icon = ''

class SocialMediaPostBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True,help_text = 'Recommended aspect ratio: 2/3 and image dimensions: 600x900')
    link = blocks.URLBlock(required=True)
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
        template = 'pages/blocks/home_page/social-media-posts-block.html'
        icon = ''


class AboutBlock(blocks.StructBlock):
    class Meta:
        template = 'pages/blocks/home_page/about-block.html'
        icon = ''


### Home/Privacy Policy/Terms & Conditions pages

class ColumnFaqItemBlock(blocks.StructBlock):
    question = blocks.CharBlock(required=True)
    answer = blocks.TextBlock(required=True)

    class Meta:
        icon = ''


class ColumnFaqBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    items = blocks.ListBlock(ColumnFaqItemBlock(required=False), required=False)

    class Meta:
        template = 'pages/blocks/faq-block.html'
        icon = ''



class ColumnButtonBlock(blocks.StructBlock):
    button_text = blocks.CharBlock()
    button_link = blocks.URLBlock(required=False)
    show_for = blocks.ChoiceBlock(choices=[
        ('desktop_mobile', 'Desktop/Mobile'),
        ('desktop', 'Desktop'),
        ('mobile', 'Mobile'),
    ], icon='cup')
    class Meta:
        template = 'pages/blocks/button-block.html'
        icon = ''

class ColumnGridItemBlock(blocks.StructBlock):
    image = ImageChooserBlock(help_text='Recommended aspect ratio: 1/1 and image dimensions: 250x250')
    text = blocks.TextBlock()
    class Meta:
        icon = ''

class ColumnGridBlock(blocks.StructBlock):
    items = blocks.ListBlock(ColumnGridItemBlock())
    class Meta:
        template = 'pages/blocks/grid-block.html'
        icon = ''

class ColumnParagraphBlock(blocks.StructBlock):
    rich_text = blocks.RichTextBlock()
    class Meta:
        template = 'pages/blocks/paragraph-block.html'
        icon = ''



class ColumnItemsBlock(blocks.StreamBlock):
    paragraph = ColumnParagraphBlock(required=False)
    faq = ColumnFaqBlock(required=False)
    button = ColumnButtonBlock(required=False)
    grid = ColumnGridBlock(required=False)
    class Meta:
        icon = ''

class ColumnBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    column = ColumnItemsBlock()
    width = blocks.ChoiceBlock(choices=[
        ('col-span-12', '100%'),
        ('col-span-7', '60%'),
        ('col-span-6', '50%'),
        ('col-span-5', '40%'),
    ], icon='cup')
    class Meta:
        icon = ''


class ColumnsBlock(blocks.StructBlock):
    columns = blocks.ListBlock(ColumnBlock())
    hide_section = blocks.BooleanBlock(required=False,label='Hide Section')
    hide_on_moya = blocks.BooleanBlock(required=False,label='Hide Section on Moya App')

    class Meta:
        template = 'pages/blocks/columns-block.html'
        icon = ''
