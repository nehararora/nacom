from django.conf import settings
from django.template.loader import render_to_string


def analytics(request):
    """
    Returns analytics code.

    :param request:
    :return:
    """
    if not settings.DEBUG:
        return {
            'analytics_code': render_to_string("analytics/analytics.html",
                                               {'google_analytics_key': settings.GOOGLE_ANALYTICS_KEY})}
    else:
        return {'analytics_code': ""}
