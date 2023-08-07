import os

def export_theme_vars(request):
    data = {}
    TAILWIND_APP_NAME = os.environ.get('TAILWIND_APP_NAME', 'apps.big_sis_theme')
    data['THEME_URL'] = TAILWIND_APP_NAME.split('.', 1)[1] + '/'
    return data