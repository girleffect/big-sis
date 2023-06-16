from social_core.exceptions import AuthForbidden
from wagtail.core.models import Site
from apps.helpers.models import GlobalSettings

def auth_allowed(user, backend, details, response, request, *args, **kwargs):
    if user and user.is_superuser:
        return
    site = Site.find_for_request(request)
    global_settings = GlobalSettings.for_site(site)
    allowed_emails = [
        str(email).lower() for email in global_settings.social_auth_allowed_emails.__iter__()
    ]
    email = details.get("email")
    allowed = False
    if email and allowed_emails:
        email = email.lower()
        allowed = email in allowed_emails
    if not allowed:
        raise AuthForbidden(backend)