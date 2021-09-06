from shrinker.models import ShortURL
from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):
  return render(request, 'shrinker/index.html')

def shrink(request):
  return

def redirect(request, short_url):
  try:
    long_url = ShortURL.objects.get(short_url=short_url)
    response = redirect(long_url)
    return response
  except:
    raise Http404('Invalid short url')