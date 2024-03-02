from django.core.cache import cache
from .models import AdvertizementFirst, AdvertizementSecond, AdvertizementThird

def advertizement_first(request):
    advertizement_first = cache.get('advertizement_first')
    if not advertizement_first:
        advertizement_first = AdvertizementFirst.objects.first()
        cache.set('advertizement_first', advertizement_first, 60*00)  

    return {'advertizement_first': advertizement_first}

def advertizement_second(request):
    advertizement_second = cache.get('advertizement_second')
    if not advertizement_second:
        advertizement_second = AdvertizementSecond.objects.first()
        cache.set('advertizement_second', advertizement_second, 60*00)  
    return {'advertizement_second': advertizement_second}

def advertizement_third(request):
    advertizement_third = cache.get('advertizement_third')
    if not advertizement_third:
        advertizement_third = AdvertizementThird.objects.first()
        cache.set('advertizement_third', advertizement_third, 60*00)  
    return {'advertizement_third': advertizement_third}

def favicon(request):
    favicon = cache.get('favicon')
    if not favicon:
        favicon = AdvertizementThird.objects.first()
        cache.set('favicon', favicon, 60*60*00)  
    return {'favicon': favicon}