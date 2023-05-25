from django.conf import settings
from django.utils import translation
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def set_language(request, code):
    try:
        referer = request.META['HTTP_REFERER']
    except KeyError:
        return HttpResponse(status=204)
    referer = referer.replace(settings.BASE_URL, '')
    translation.activate(code)
    translated_url = f'/{code}/{referer}'
    return HttpResponseRedirect(translated_url)