from django.db import models
from django.conf import settings
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList, MultiFieldPanel
from wagtail.images.models import Image, AbstractImage, AbstractRendition
from apps.pages import blocks as pages_blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock

class CustomImage(AbstractImage):
    admin_form_fields = Image.admin_form_fields + (
    )


class CustomRendition(AbstractRendition):
    image = models.ForeignKey(CustomImage, on_delete=models.CASCADE, related_name='renditions')

    class Meta:
        unique_together = (
            ('image', 'filter_spec', 'focal_point_key'),
        )



class HomePage(Page):
    max_count = 2
    parent_page_types = ['wagtailcore.Page']
    template_name = 'pages/home_page.html'
    header_title = models.CharField(max_length=255, blank=True)
    header_subtitle = models.TextField(blank=True)
    header_background_image = StreamField([
        ('Image', ImageChooserBlock(help_text='Recommended aspect ratio: 16/9 and image dimensions: 1920x1080')),
        ('Document', DocumentChooserBlock()),

    ],use_json_field=False, blank=True, min_num=0, max_num=1, collapsed=True,
        block_counts={
            'Image': {'min_num': 0, 'max_num': 1},
            'Document': {'min_num': 0, 'max_num': 1},
        },
    )
    header_left_side_image = StreamField([
        ('Image', ImageChooserBlock(help_text='Recommended aspect ratio: 16/9 and minimum width 900px')),
        ('Document', DocumentChooserBlock()),

    ],use_json_field=False, blank=True, min_num=0, max_num=1,verbose_name='Header left side image', collapsed=True,
        block_counts={
            'Image': {'min_num': 0, 'max_num': 1},
            'Document': {'min_num': 0, 'max_num': 1},
        },
    )
    header_image = StreamField([
        ('Image', ImageChooserBlock(help_text='Recommended aspect ratio: 1/1 and minimum width 900px')),
        ('Document', DocumentChooserBlock()),

    ],use_json_field=False, blank=True, min_num=0, max_num=1,verbose_name='Header right side image', collapsed=True,
        block_counts={
            'Image': {'min_num': 0, 'max_num': 1},
            'Document': {'min_num': 0, 'max_num': 1},
        },
    )
    whatsapp_link = models.CharField(max_length=255,blank=True)
    whatsapp_link_text = models.TextField(blank=True)
    messenger_link = models.CharField(max_length=255,blank=True)
    messenger_link_text = models.TextField(blank=True)
    moya_link = models.CharField(max_length=255,blank=True)
    moya_link_text = models.TextField(blank=True)
    seo_image = models.ForeignKey(
        settings.WAGTAILIMAGES_IMAGE_MODEL,
        verbose_name='Seo image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='The image displayed when a page gets posted on social media.'
    )
    body = StreamField([
        ('Featured_Blog_Post_Section', pages_blocks.FeaturedBlogPostBlock()),
        ('Columns_Section', pages_blocks.ColumnsBlock()),
        ('Social_Media_Posts_Section', pages_blocks.SocialMediaPostsBlock()),
        ('Latest_Blog_Posts_Section', pages_blocks.LatestBlogPostsBlock()),

    ],use_json_field=False, blank=True, min_num=0, max_num=4, collapsed=True,
        block_counts={
            'Featured_Blog_Post_Section': {'min_num': 0, 'max_num': 1},
            'Columns_Section': {'min_num': 0, 'max_num': 1},
            'Social_Media_Posts_Section': {'min_num': 0, 'max_num': 1},
            'Latest_Blog_Posts_Section': {'min_num': 0, 'max_num': 1},
        },
    )
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('header_title'),
                FieldPanel('header_subtitle'),
                FieldPanel('header_background_image'),
                FieldPanel('header_left_side_image'),
                FieldPanel('header_image'),
                FieldPanel('whatsapp_link'),
                FieldPanel('whatsapp_link_text'),
                FieldPanel('messenger_link'),
                FieldPanel('messenger_link_text'),
                FieldPanel('moya_link'),
                FieldPanel('moya_link_text'),
            ],
            heading="Header Section",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('body'),
            ],
            heading="Body Section",
            classname="collapsible"
        ),

    ]
    promote_panels = [
        MultiFieldPanel(
            [
                FieldPanel('slug'),
                FieldPanel('seo_title'),
                FieldPanel('search_description'),
                FieldPanel('seo_image'),
            ],
            heading="For search engines",
            classname="collapsible"
        ),

    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings'),
    ])

    class Meta:
        verbose_name = "Home page"

# The About page.This page is used for providing timeline,testimonials,key figures and faq information to end users with the help of wagtail streamfield field.
class AboutPage(Page):
    max_count = 1
    parent_page_types = ['pages.HomePage']
    template_name = 'pages/about_page.html'
    header_title = models.CharField(max_length=255, blank=True)
    header_subtitle = models.TextField(blank=True)
    header_image = models.ForeignKey(
        settings.WAGTAILIMAGES_IMAGE_MODEL,
        verbose_name='Header image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Recommended aspect ratio: 7/6 and image dimensions: 630x540'
    )
    seo_image = models.ForeignKey(
        settings.WAGTAILIMAGES_IMAGE_MODEL,
        verbose_name='Seo image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='The image displayed when a page gets posted on social media.'
    )
    body = StreamField([
        ('Time_Line_Section', pages_blocks.TimeLineBlock()),
        ('Key_Figures_And_Testimonials_Section', pages_blocks.KeyFiguresAndTestimonialsBlock()),
        ('Faq_Section', pages_blocks.FaqBlock()),

    ],use_json_field=False,blank=True, min_num=0, max_num=3, collapsed=True,
        block_counts={
            'Time_Line_Section': {'min_num': 0, 'max_num': 1},
            'Key_Figures_And_Testimonials_Section': {'min_num': 0, 'max_num': 1},
            'Faq_Section': {'min_num': 0, 'max_num': 1},
        },
    )
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('header_title'),
                FieldPanel('header_subtitle'),
                FieldPanel('header_image'),
            ],
            heading="Header Section",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('body'),
            ],
            heading="Body Section",
            classname="collapsible"
        ),

    ]
    promote_panels = [
        MultiFieldPanel(
            [
                FieldPanel('slug'),
                FieldPanel('seo_title'),
                FieldPanel('search_description'),
                FieldPanel('seo_image'),
            ],
            heading="For search engines",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('show_in_menus'),
            ],
            heading="For site menus",
            classname="collapsible"
        ),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings'),
    ])

    class Meta:
        verbose_name = "About page"

# The Content page.This page is used for creating general purpose pages e.g a privacy policy.
class ContentPage(Page):
    parent_page_types = ['pages.HomePage']
    template_name = 'pages/content_page.html'
    seo_image = models.ForeignKey(
        settings.WAGTAILIMAGES_IMAGE_MODEL,
        verbose_name='Seo image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='The image displayed when a page gets posted on social media.'
    )
    body = StreamField([
        ('Columns_Section', pages_blocks.ColumnsBlock()),

    ],use_json_field=False, blank=True, min_num=0, max_num=1, collapsed=True,
        block_counts={
            'Columns_Section': {'min_num': 0, 'max_num': 1},
        },
    )
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
    promote_panels = [
        MultiFieldPanel(
            [
                FieldPanel('slug'),
                FieldPanel('seo_title'),
                FieldPanel('search_description'),
                FieldPanel('seo_image'),
            ],
            heading="For search engines",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('show_in_menus'),
            ],
            heading="For site menus",
            classname="collapsible"
        ),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings'),
    ])
    class Meta:
        verbose_name = "Content page"



