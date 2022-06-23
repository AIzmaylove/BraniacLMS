from turtle import title
from django.urls import reverse
from unittest import result
from django.test import TestCase, Client
from http import HTTPStatus
from authapp.models import User

from mainapp.models import News

class StaticPagesSmokeTest(TestCase):
    
    def test_page_index_open(self):
        url = reverse('mainapp:index')
        result = self.client.get(url)

        self.assertAlmostEqual(result.status_code, HTTPStatus.OK)

    def test_page_contacts_open(self):
        url = reverse('mainapp:contacts')
        result = self.client.get(url)

        self.assertAlmostEqual(result.status_code, HTTPStatus.OK)


class NewsTestCase(TestCase):

    def setUp(self) -> None:
        for i in range(10):
            News.objects.create(
                title=f'News1{i}',
                intro=f'Intro1{i}',
                body=f'Body1{i}'
            )
        
        User.objects.create_superuser(username='django1', password='geekbrains')
        self.client_with_auth = Client()
        auth_url = reverse('authapp:login')
        self.client_with_auth.post(
            auth_url,
            {'username': 'django1', 'password': 'geekbrains'}
        )

    def test_open_page(self):
        url = reverse('mainapp:news')
        result = self.client.get(url)

        self.assertEqual(result.status_code, HTTPStatus.OK)

    def test_failed_open_add_by_anonym(self):
        url = reverse('mainapp:news_create')
        result = self.client.get(url)

        self.assertEqual(result.status_code, HTTPStatus.FOUND)

