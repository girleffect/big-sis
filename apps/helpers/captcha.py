from django.conf import settings
import requests

def verify_captcha(token):
    payload = {'secret': settings.CAPTCHA_SECRET_KEY,'response':token}
    r = requests.post("https://www.google.com/recaptcha/api/siteverify", data=payload)
    status_code = r.status_code
    if status_code == 200:
        status = r.json()['success']
        if str(status) == 'True':
            return True
        else:
            return False
    else:
        return False