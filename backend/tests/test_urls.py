from django.test import SimpleTestCase
from django.urls import reverse, resolve
from backend.views import CategoryList, CategoryDetail


class TestUrls(SimpleTestCase):

    def test_category_url_is_resolves(self):
        url = reverse('category')
        assert resolve(url).func.view_class == CategoryList

    def test_category_details_url_is_resolves(self):
        url = reverse('category_details', args=[1])
        assert resolve(url).func.view_class == CategoryDetail
