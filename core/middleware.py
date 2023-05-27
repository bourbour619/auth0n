from django.conf import settings
from django.utils import translation

class LanguageMiddelware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            del request.META['HTTP_ACCEPT_LANGUAGE']
        except KeyError:
            pass
        
        response = self.get_response(request)
        
        return response