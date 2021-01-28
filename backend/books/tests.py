from django.test import TestCase
from rest_framework import status
import requests


class URLTests(TestCase):
    def test_homepage(self):
        response = requests.get(url="http://localhost:8000/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_url(self):
        r = requests.get("http://localhost:8000/book/")
        self.assertEqual(r.status_code, status.HTTP_200_OK)

    def test_login_url(self):
        r = requests.get("http://localhost:8000/login/")
        self.assertEqual(r.status_code, status.HTTP_200_OK)

    def test_genre_url(self):
        r = requests.get("http://localhost:8000/genre/")
        self.assertEqual(r.status_code, status.HTTP_200_OK)
