from django.conf import settings


def export_settings(request):
    # return any necessary values
    return {
        'REGISTRATION_OPEN': settings.REGISTRATION_OPEN,
        'PAYPAL_BUTTON_ID': settings.PAYPAL_BUTTON_ID,
    }