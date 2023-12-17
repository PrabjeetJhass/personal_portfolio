from django.shortcuts import render, redirect
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.http import JsonResponse, HttpResponseBadRequest
from .models import ShortenedLink
import string, random, json

def validate_url(url):
    if 'https://' in url or 'http://' in url:
        return url
    
    else:
        url = 'https://' + url
        return url

def index_view(request):
    return render(request, 'indexl.html')

def shortenUrl(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == 'POST':
        shortUrlSlug = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=5))
        
        longUrl = json.load(request).get('longUrl')

        longUrl = validate_url(longUrl)

        validate = URLValidator()

        try:
            validate(longUrl)
            shortenedUrl = ShortenedLink.objects.create(shortUrl=shortUrlSlug, longUrl=longUrl)
            shortenedUrl.save()

            return JsonResponse({'type': 'success', 'ShortUrl': shortUrlSlug})
        except:
            return JsonResponse({'type': 'error', 'message': 'invalid URL'})

    return HttpResponseBadRequest('Bad Request')

def redirectTo(request, shortUrl):
    isShortUrlValid = ShortenedLink.objects.filter(shortUrl=shortUrl).exists()

    if isShortUrlValid:
        redirectSite = ShortenedLink.objects.get(shortUrl=shortUrl).longUrl
    else:
        redirectSite = 'shortenURL'

    return redirect(redirectSite)