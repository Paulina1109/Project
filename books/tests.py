from django.test import TestCase
from .models import *


class SimpleTest(TestCase):
    def test_details(self):
        response = self.client.get('/my-list/')
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        response = self.client.get('/add-recommendation/')
        self.assertEqual(response.status_code, 200)

class GenreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Genre.objects.create(title='Big World', genre='Motivational')

    def test_title_label(self):
        genre = Genre.objects.get(id=1)
        field_label = genre._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_genre_label(self):
        genre = Genre.objects.get(id=1)
        field_label = genre._meta.get_field('genre').verbose_name
        self.assertEqual(field_label, 'genre')

    def test_title_max_length(self):
        title = Genre.objects.get(id=1)
        max_length = title._meta.get_field('title').max_length
        self.assertEqual(max_length, 64)


