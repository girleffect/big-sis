from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django import forms
from django.shortcuts import render
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList, MultiFieldPanel
from modelcluster.fields import ParentalManyToManyField

# The service finder page.This page is used for listing and filtering all the service pages(Clinics)
class ServiceFinderPage(Page):
    max_count = 1
    parent_page_types = ['pages.HomePage']
    template_name = 'services/service_finder_page.html'
    header_title = models.CharField(max_length=255, blank=True)
    header_subtitle = models.TextField(blank=True)
    header_youtube_video_id = models.CharField(max_length=255,blank=True)
    header_video_poster = models.ForeignKey(
        settings.WAGTAILIMAGES_IMAGE_MODEL,
        verbose_name='Header youtube video poster',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Recommended aspect ratio 16:9 and image dimensions 320x180'
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

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('header_title'),
                FieldPanel('header_subtitle'),
                FieldPanel('header_youtube_video_id'),
                FieldPanel('header_video_poster'),
            ],
            heading="Header Section",
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

    def serve(self, request, *args, **kwargs):
        from apps.services.forms import ServiceFinderForm
        context = self.get_context(request)
        if 'submit' in request.GET:
            form = ServiceFinderForm(request.GET)
            if form.is_valid():
                location = form.cleaned_data['location']
                service_types = form.cleaned_data['service_type']
                if location and service_types:
                    services = ServicePage.objects.live().filter(location=location).filter(service_type__in=service_types).distinct()
                elif location:
                    services = ServicePage.objects.live().filter(location=location).distinct()
                elif service_types:
                    services = ServicePage.objects.live().filter(
                        service_type__in=service_types).distinct()
                else:
                    services = ServicePage.objects.live()[:6]
                context['services'] = services
        else:
            form = ServiceFinderForm()
            context['services'] = ServicePage.objects.live()[:6]
        context['form'] = form
        return render(
            request,
            self.template_name,
            context
        )


    class Meta:
        verbose_name = "Service finder page"

# This class is used for associating a service page(clinic) with a location.
class ServiceLocation(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField()
    order = models.PositiveIntegerField(default=0)
    panels = [
        FieldPanel('name'),
        FieldPanel('order'),
    ]
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'


    class Meta:
        verbose_name = "Service Location"
        verbose_name_plural = "Service Locations"
        ordering = ['order']


# This class is used to associate a service page(clinic) with a service type e.g Telemedicine.
class ServiceType(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField()
    order = models.PositiveIntegerField(default=0)
    panels = [
        FieldPanel('name'),
        FieldPanel('order'),
    ]
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'


    class Meta:
        verbose_name = "Service Type"
        verbose_name_plural = "Service Types"
        ordering = ['order']

# The service page(clinic).This page is used for providing info about a clinic to end users.
class ServicePage(Page):
    parent_page_types = ['services.ServiceFinderPage']
    subpage_types = []
    template_name = 'services/service_page.html'
    preview_text = models.TextField(blank=True,help_text='If populated the text will be displayed on the service finder page.If omitted the first 50 words of the below text field will be displayed.')
    text = RichTextField(blank=True)
    price = models.CharField(max_length=255,blank=True)
    phone = models.CharField(max_length=255,blank=True)
    address = models.TextField(blank=True)
    google_maps_address = models.URLField(max_length=500,blank=True)
    messenger_link = models.URLField(blank=True)
    website = models.URLField(blank=True)
    service_type = ParentalManyToManyField(ServiceType, blank=True)
    location = models.ForeignKey(ServiceLocation,null=True,blank=True,on_delete=models.SET_NULL,related_name='services',verbose_name='Service Location')
    seo_image = models.ForeignKey(
        settings.WAGTAILIMAGES_IMAGE_MODEL,
        verbose_name='Seo Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='The image displayed when a page gets posted on social media.'
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('preview_text'),
                FieldPanel('text'),
                FieldPanel('location'),
                FieldPanel('service_type', widget=forms.CheckboxSelectMultiple),
                FieldPanel('price'),
                FieldPanel('phone'),
                FieldPanel('address'),
                FieldPanel('google_maps_address'),
                FieldPanel('messenger_link'),
                FieldPanel('website'),

            ],
            heading="Details Section",
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
        verbose_name = "Service page"