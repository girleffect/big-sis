from django.db import models
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import Http404
from django.conf import settings
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, TabbedInterface, ObjectList, MultiFieldPanel
from wagtail.fields import RichTextField,StreamField
from apps.blog import blocks as blog_blocks
import datetime
from django.http import HttpResponse
from apps.helpers.captcha import verify_captcha

# The blog index page.This page is used for listing all the post pages.
class BlogIndexPage(Page):
    max_count = 1
    template_name = 'blog/blog_index_page.html'
    parent_page_types = ['pages.HomePage']
    subpage_types = ['blog.BlogCategoryPage']
    seo_image = models.ForeignKey(
        settings.WAGTAILIMAGES_IMAGE_MODEL,
        verbose_name='Seo image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='The image displayed when a page gets posted on social media.'
    )
    featured_post = models.ForeignKey('blog.PostPage',null=True,blank=True,on_delete=models.SET_NULL,help_text='If populated the featured post will be displayed at Blog Index page and Blog Category Pages.')
    body = StreamField([
        ('Social_Media_Posts_Section', blog_blocks.SocialMediaPostsBlock()),


    ],use_json_field=False, blank=True, min_num=0, max_num=1, collapsed=True,
        block_counts={
            'Social_Media_Posts_Section': {'min_num': 0, 'max_num': 1},
        },
    )
    show_posts_social_media_share_links = models.BooleanField(default=True)
    show_posts_like_button = models.BooleanField(default=True)
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('featured_post'),
            ],
            heading="Featured Post Section",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('body'),
            ],
            heading="Body Section",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('show_posts_social_media_share_links'),
                FieldPanel('show_posts_like_button'),
            ],
            heading="Posts Share/Like Buttons",
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
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        today = datetime.datetime.today()
        posts = PostPage.objects.live().filter(published_on__lte=today).order_by('-published_on')
        paginator = Paginator(posts, 8)  # Show 8 posts per page
        page = request.GET.get('page')
        context['posts'] = paginator.get_page(page)
        if self.featured_post:
            context['featured_post'] = self.featured_post
        return context

    class Meta:
        verbose_name = "Blog index page"


# The blog category page.This page is used for listing all it's child post pages.
class BlogCategoryPage(Page):
    template_name = 'blog/blog_category_page.html'
    parent_page_types = ['blog.BlogIndexPage']
    subpage_types = ['blog.PostPage']
    seo_image = models.ForeignKey(
        settings.WAGTAILIMAGES_IMAGE_MODEL,
        verbose_name='Seo image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='The image displayed when a page gets posted on social media.'
    )
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
        ObjectList(Page.content_panels, heading='Content'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings'),
    ])
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        today = datetime.datetime.today()
        posts = PostPage.objects.descendant_of(self).live().filter(published_on__lte=today).order_by('-published_on')
        paginator = Paginator(posts, 8)  # Show 8 posts per page
        page = request.GET.get('page')
        context['posts'] = paginator.get_page(page)
        if self.get_parent().specific.featured_post:
            context['featured_post'] = self.get_parent().specific.featured_post
        return context

    class Meta:
        verbose_name = "Blog category page"


# The post page.This page is used for providing news,announcements and information to end users.
class PostPage(Page):
    template_name = 'blog/post_page.html'
    parent_page_types = ['blog.BlogCategoryPage']
    subpage_types = []
    published_on = models.DateTimeField(verbose_name="Published On", default=datetime.datetime.today,help_text='If a future date is choosen then the post will not be shown to the end users until the date specified.')
    image = models.ForeignKey(
        settings.WAGTAILIMAGES_IMAGE_MODEL,
        verbose_name='Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text = 'Recommended aspect ratio: 1/1 and image dimensions: 500x500'
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
    preview_text = models.TextField(blank=True)
    text = RichTextField(blank=True)
    hit_counter = models.PositiveIntegerField(default=1)
    content_panels = Page.content_panels + [
        FieldPanel('published_on'),
        FieldPanel('image'),
        FieldPanel('preview_text'),
        FieldPanel('text'),
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

    def show_social_media_share_buttons(self):
        blog_index_page = BlogIndexPage.objects.live().first().specific
        if blog_index_page:
            if blog_index_page.show_posts_social_media_share_links:
                return True
        return False

    def show_like_button(self):
        blog_index_page = BlogIndexPage.objects.live().first().specific
        if blog_index_page:
            if blog_index_page.show_posts_like_button:
                return True
        return False

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['siblings'] = PostPage.objects.sibling_of(self, inclusive=False).live().order_by(
            '-published_on')[:2]
        return context

    def serve(self, request, *args, **kwargs):
        context = self.get_context(request)
        published_on = self.published_on
        today = datetime.datetime.today()
        if published_on > today and request.user.is_anonymous:
            raise Http404

        if f'user_has_liked_post_{self.id}' in request.session:
            context['user_has_liked_post'] = 'true'
        else:
            context['user_has_liked_post'] = 'false'


        if 'update_hit_counter' in request.GET:
            captcha_token = request.GET.get('captcha_token', None)
            if captcha_token:
                captcha_verified = verify_captcha(captcha_token)
                if captcha_verified:
                    add_to_hit_counter = request.GET.get('update_hit_counter')
                    if add_to_hit_counter == 'true':
                        if not f'user_has_liked_post_{self.id}' in request.session:
                            self.hit_counter += 1
                            request.session[f'user_has_liked_post_{self.id}'] = True
                    else:
                        if f'user_has_liked_post_{self.id}' in request.session:
                            del request.session[f'user_has_liked_post_{self.id}']
                            self.hit_counter -= 1
                    self.save()
            return HttpResponse(self.hit_counter)
        context['absolute_uri'] = request.build_absolute_uri()
        return render(
            request,
            self.template_name,
            context
        )
    class Meta:
        verbose_name = "Post page"
