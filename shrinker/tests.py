from django.http import response
from django.test import Client, TestCase
from shrinker.models import ShortURL

# Create your tests here.
class ShortURLTestCase(TestCase):
  def setUp(self):
    url_object = ShortURL(long_url='https://www.google.com')
    url_object.save()
    self.short_url_object = url_object
    
    self.client = Client()

  def test_index_view(self):
    response = self.client.get('/')
    assert response.status_code == 200

  def test_redirect(self):
    response = self.client.get(f'/{self.short_url_object.short_url}')
    assert response.status_code == 302