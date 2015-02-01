from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page

# Create your tests here.

class HomePageTest(TestCase):
    def test_root_url_resovles_to_home_page_view(self):
        found = resolve("/")
        self.assertEquals(found.func, home_page)
