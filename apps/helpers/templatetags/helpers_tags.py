from wagtail.models import Page
from wagtail.models import Site
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
def get_in_menu_pages(request):
    site = Site.find_for_request(request)
    homepage = HomePage.objects.live().filter(sites_rooted_here=site).first()
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
    if 'request' in context and context['request'].session.get('moya') == True:
        return True
    return False


@register.simple_tag(takes_context=True)
def display_sessions(context):
    if 'request' in context:
        session_data = dict(context['request'].session.items())
        print(session_data)
        return session_data
    return False