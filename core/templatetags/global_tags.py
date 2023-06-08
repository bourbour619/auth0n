import datetime
from django import template
from django.conf import settings
import re

register = template.Library()


@register.simple_tag(takes_context=True)
def get_i18n_path(context, lang_code):
    path = context['request'].get_full_path()
    for code, name in settings.LANGUAGES:
        if code in path:
            path = re.sub(f'\/{code}', '', path)
    if lang_code != settings.LANGUAGE_CODE:
        path = f'/{lang_code}{path}'
    return path


@register.inclusion_tag("dummy.html", takes_context=True)
def render_template(context, template_dir, *args, **kwargs):
    c = { 'template_dir': template_dir }
    return c | kwargs if kwargs else c