from django.http import response
from django.test import Client, TestCase, SimpleTestCase
from shrinker.models import ShortURL

# Create your tests here.
class ShortURLTestCase(TestCase):
  def setUp(self):
    # Creates and saves ShortURL object to database
    url_object = ShortURL(long_url='https://www.google.com')
    url_object.save()
    self.short_url_object = url_object
    
    self.client = Client()

  def test_index_view(self):
    response = self.client.get('/')
    assert response.status_code == 200

  def test_redirect(self):
    # Retrieves long url from database and redirects user
    response = self.client.get(f'/{self.short_url_object.short_url}')
    long_url = self.short_url_object.long_url
    SimpleTestCase.assertRedirects(self, response=response, expected_url=long_url, 
                                   status_code=302, target_status_code=302, 
                                   msg_prefix='', fetch_redirect_response=True)
