from django.test import TestCase, Client
from django.urls import reverse
from shop.models import Category


class TestCategoryViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('category')
        self.details_url = reverse('category_details', args=[1])

    def test_category_list_get(self):
        response = self.client.get(self.list_url)
        assert response.status_code == 200

    def test_category_details_get(self):
        Category.objects.create(title='demo')
        response = self.client.get(self.details_url)
        assert response.status_code == 200

    def test_categories_post_unauthorized(self):
        response = self.client.post(self.list_url, {'title': 'blah'})
        assert response.status_code == 401
