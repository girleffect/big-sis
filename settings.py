# This is a fairly standard Django settings file, with some special additions
# that allow addon applications to auto-configure themselves. If it looks
# unfamiliar, please see our documentation:
#
#   http://docs.divio.com/en/latest/reference/configuration-settings-file.html
#
# and comments below.


# INSTALLED_ADDONS is a list of self-configuring Divio Cloud addons - see the
# Addons view in your project's dashboard. See also the addons directory in
# this project, and the INSTALLED_ADDONS section in requirements.in.

INSTALLED_ADDONS = [
    # Important: Items listed inside the next block are auto-generated.
    # Manual changes will be overwritten.
    # <INSTALLED_ADDONS>  # Warning: text inside the INSTALLED_ADDONS tags is auto-generated. Manual changes will be overwritten.
    'aldryn-addons',
    'aldryn-django',
    'aldryn-sso',
    'aldryn-wagtail',
    # </INSTALLED_ADDONS>
]

# Now we will load auto-configured settings for addons. See:
#
#   http://docs.divio.com/en/latest/reference/configuration-aldryn-config.html
#
# for information about how this works.
#
# Note that any settings you provide before the next two lines are liable to be
# overwritten, so they should be placed *after* this section.
import os
import aldryn_addons.settings

aldryn_addons.settings.load(locals())

# Your own Django settings can be applied from here on. Key settings like
# INSTALLED_APPS, MIDDLEWARE and TEMPLATES are provided in the Aldryn Django
# addon. See:
#
#   http://docs.divio.com/en/latest/how-to/configure-settings.html
#
# for guidance on managing these settings.

INSTALLED_APPS.extend(
    [
        'wagtail.contrib.settings',
        'rest_framework',
        "wagtail.contrib.routable_page",
        'tailwind',
        'django_browser_reload',
        'social_django',
        'apps.pages',
        'apps.services',
        'apps.blog',
        'apps.helpers',
    ]
)

STAGE = os.environ.get('STAGE',None)

# MIDDLEWARE settings
MIDDLEWARE.append("apps.pages.middleware.DatafreeMiddleware")
if STAGE == 'local':
    MIDDLEWARE.append("django_browser_reload.middleware.BrowserReloadMiddleware")
    MIDDLEWARE.pop(0)


# Wagtail settings
WAGTAILADMIN_BASE_URL = 'http://bigsis.co.za'
WAGTAIL_ALLOW_UNICODE_SLUGS = False
WAGTAIL_ENABLE_UPDATE_CHECK = False
WAGTAIL_ENABLE_WHATS_NEW_BANNER = False
WAGTAIL_MODERATION_ENABLED = False
WAGTAIL_WORKFLOW_ENABLED = False
WAGTAILIMAGES_JPEG_QUALITY = 65
WAGTAILIMAGES_WEBP_QUALITY = 65
WAGTAILIMAGES_IMAGE_MODEL = 'pages.CustomImage'
WAGTAILIMAGES_FORMAT_CONVERSIONS = {
    'bmp': 'jpeg',
    'webp': 'webp',
}


WAGTAILADMIN_RICH_TEXT_EDITORS = {
    'default': {
        'WIDGET': 'wagtail.admin.rich_text.DraftailRichTextArea',
        'OPTIONS': {
            'features': ['h1', 'h2', 'h3', 'h4', 'h5','h6','bold','italic','ol','ul','hr','link','document-link','image','embed','code','superscript','subscript','strikethrough','blockquote']
        }
    },
}

# Social Auth settings
SOCIAL_AUTH_JSONFIELD_ENABLED = True
SOCIAL_AUTH_URL_NAMESPACE = 'social'
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY', '')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET', '')

LOGIN_URL = '/login/google-oauth2/'

LOGIN_REDIRECT_URL = '/admin/'
LOGOUT_REDIRECT_URL = '/'

MIDDLEWARE.append("social_django.middleware.SocialAuthExceptionMiddleware")

SOCIAL_AUTH_PIPELINE = (
    "social_core.pipeline.social_auth.social_details",
    "social_core.pipeline.social_auth.social_uid",
    "social_core.pipeline.social_auth.social_user",
    "apps.pipeline.auth_allowed",
    "social_core.pipeline.user.get_username",
    "social_core.pipeline.social_auth.associate_by_email",
    "social_core.pipeline.user.create_user",
    "social_core.pipeline.social_auth.associate_user",
    "social_core.pipeline.social_auth.load_extra_data",
    "social_core.pipeline.user.user_details",
)

# Tailwind settings

if STAGE == 'local':
    TAILWIND_DEV_MODE = True
else:
    TAILWIND_DEV_MODE = False
TAILWIND_APP_NAME = os.environ.get('TAILWIND_APP_NAME','apps.big_sis_theme')
print(TAILWIND_APP_NAME)
INSTALLED_APPS.append(TAILWIND_APP_NAME)
print(INSTALLED_APPS)
INTERNAL_IPS = [
    "127.0.0.1",
]
TAILWIND_FOLDER_NAME =TAILWIND_APP_NAME.split('.',1)[1]
print(TAILWIND_FOLDER_NAME)
TAILWIND_CSS_PATH = f'css/{TAILWIND_FOLDER_NAME}/dist/styles.css'
print(TAILWIND_CSS_PATH)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'apps',TAILWIND_FOLDER_NAME, 'static/'),
]

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

TEMPLATE_CONTEXT_PROCESSORS = [
   "django.core.context_processors.request"
]

# Logging settings
ADMINS = (
    ('Kyriakos Toumbas', 'webmaster@pixelactions.com'),
    ('Nicolas Christofi', 'nicolas@pixelactions.com'),
)
MANAGERS = ADMINS


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

