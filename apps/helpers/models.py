from django.db import models
from wagtail.models import Page, Orderable, ClusterableModel
from modelcluster.fields import ParentalKey
from wagtail.fields import RichTextField,StreamField
from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList, MultiFieldPanel,InlinePanel,FieldRowPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock

# This class is used for providing an easy way to edit the footer content and to add scripts to the head and body of the html.
@register_setting
class GlobalSettings(BaseSetting,ClusterableModel):
    ga_measurement_id = models.CharField(max_length=512, blank=True, null=True)
    text = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    facebook_url = models.URLField(blank=True)
    tiktok_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    background_image = StreamField([
        ('Image', ImageChooserBlock()),
        ('Document', DocumentChooserBlock()),

    ],use_json_field=False, blank=True, min_num=0, max_num=1, collapsed=True,
        block_counts={
            'Image': {'min_num': 0, 'max_num': 1},
            'Document': {'min_num': 0, 'max_num': 1},
        },
    )
    sitemap = StreamField([
        ('Links', blocks.ListBlock(blocks.PageChooserBlock())),

    ],use_json_field=False, blank=True, min_num=0, max_num=1, collapsed=True,
        block_counts={
            'Links': {'min_num': 0, 'max_num': 1},
        },
    )
    social_auth_allowed_emails = StreamField(
        [
            ("email_address", blocks.EmailBlock()),
        ], use_json_field=False, blank=True,
    )
    scripts_panel = [
        MultiFieldPanel(
            [
                FieldPanel("ga_measurement_id"),
                InlinePanel('scripts', label="Script"),
            ],
            heading="Scripts",
            classname="collapsible"
        ),


    ]
    footer_panel = [
        MultiFieldPanel(
            [
                FieldPanel('text'),
                FieldPanel('email'),
                FieldPanel('facebook_url'),
                FieldPanel('tiktok_url'),
                FieldPanel('instagram_url'),
                FieldPanel('twitter_url'),
                FieldPanel('youtube_url'),
                FieldPanel('background_image'),
                FieldPanel('sitemap')
            ],
            heading="Footer",
            classname="collapsible"
        ),


    ]
    social_auth_panel = [
        MultiFieldPanel(
            [
                FieldPanel('social_auth_allowed_emails'),
            ],
            heading="Google sign up",
            classname="collapsible"
        ),


    ]
    edit_handler = TabbedInterface([
        ObjectList(scripts_panel, heading='Scripts'),
        ObjectList(footer_panel, heading='Footer'),
        ObjectList(social_auth_panel, heading='Social Auth'),
    ])

    class Meta:
        verbose_name = 'Global Settings'

class ThirdPartyScript(Orderable):
    page = ParentalKey(GlobalSettings, on_delete=models.CASCADE, related_name='scripts')
    script = models.TextField()
    POSITION_LIST = [
        ('head','Head'),
        ('body', 'Body'),
    ]
    position = models.CharField(max_length=255,default='head',choices=POSITION_LIST)
    hide_on_moya = models.BooleanField(default=False, help_text='Do not load Script on Moya App')