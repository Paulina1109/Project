from django.test import TestCase

from books.models import Genre

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

    # def test_object_name_is_last_name_comma_first_name(self):
    #     author = Author.objects.get(id=1)
    #     expected_object_name = f'{author.last_name}, {author.first_name}'
    #     self.assertEqual(str(author), expected_object_name)
    #
    # def test_get_absolute_url(self):
    #     author = Author.objects.get(id=1)
    #     # This will also fail if the urlconf is not defined.
    #     self.assertEqual(author.get_absolute_url(), '/catalog/author/1')
