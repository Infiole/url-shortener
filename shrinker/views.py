from shrinker.models import ShortURL
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

from .models import ShortURL
from .forms import ShortURLForm

def index(request):
  template = 'shrinker/index.html'
  context = {}
  context['form'] = ShortURLForm()

  # Normal access to index page
  if request.method == 'GET':
    return render(request, template, context)

  # User submits url to be shrinked
  elif request.method == 'POST':
    submitted_form = ShortURLForm(request.POST)
    # Validate form before saving
    if submitted_form.is_valid():
      short_url_obj = submitted_form.save()

      shrinked_url = request.build_absolute_uri('/') + short_url_obj.short_url
      long_url = short_url_obj.long_url 

      context['shrinked_url']  = shrinked_url
      context['long_url'] = long_url
      return render(request, template, context)

    context['errors'] = submitted_form.errors
  return render(request, template, context)

# User uses shrinked url
def redirect(request, short_url: str):
  try:
    short_url_obj = ShortURL.objects.get(short_url=short_url)
    return HttpResponseRedirect(short_url_obj.long_url)
  except:
    raise Http404('Invalid short url')