import aldryn_addons.urls
from aldryn_django.utils import i18n_patterns
from django.urls import include, path,re_path
from django.conf import settings
from wagtail.images.views.serve import ServeView
from apps.api import urls as api_urls
from apps.helpers.view import data_switch


if settings.STAGE == 'local':
    browser_reload_patterns = [
        path("__reload__/", include("django_browser_reload.urls")),
    ]
else:
    browser_reload_patterns = [
    ]
urlpatterns = (
        [
            re_path(r'^images/([^/]*)/(\d*)/([^/]*)/[^/]*$', ServeView.as_view(action='redirect'),
                    name='wagtailimages_serve'),
            path('api/', include(api_urls)),
            path('', include('social_django.urls', namespace='social')),
            path('data_switch/', data_switch, name='data_switch'),
        ]
        + browser_reload_patterns
        + aldryn_addons.urls.patterns()
        + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
)
