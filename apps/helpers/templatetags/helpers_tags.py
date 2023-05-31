from wagtail.models import Page
from django import template
from django.conf import settings
from apps.pages.models import HomePage
from apps.blog.models import PostPage

register = template.Library()



@register.simple_tag()
def get_stage():
    stage = settings.STAGE
    return stage

@register.simple_tag()
def get_in_menu_pages():
    homepage = Page.objects.exact_type(HomePage).first()
    if homepage:
        pages = Page.objects.live().in_menu().child_of(homepage)
        return pages
    else:
        return None

@register.simple_tag()
def get_latest_blog_post(featured_blog_post=None):
    if featured_blog_post:
        return featured_blog_post
    else:
        page = PostPage.objects.live().order_by('-published_on').first()
        return page

@register.simple_tag()
def get_latest_blog_posts(count):
    pages = PostPage.objects.live().order_by('-published_on')[:count]
    return pages

@register.simple_tag(takes_context=True)
def check_for_moya_app(context):
    if (context.request.session.get('moya') == True):
        return True
    return False