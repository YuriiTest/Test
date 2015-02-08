from django.conf import settings


def settings_processor(request):
    """Adds django.settings context variables to the context."""
    result = {}
    for elements in dir(settings):
        result[elements] = getattr(settings, elements)
    return result