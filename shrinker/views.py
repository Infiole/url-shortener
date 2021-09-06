from shrinker.models import ShortURL
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return render(request, 'shrinker/index.html')

def redirect(request, short_url):
  long_url = ShortURL.objects.get(pk=short_url)
  response = redirect(long_url)
  return response