from django.test import TestCase

from playlists.models import Playlist
from .models import Category


class CategoryTestCase(TestCase):
    def setUp(self):
        cat_a = Category.objects.create(title='Umbanda')
        cat_b = Category.objects.create(title='Kimbanda', activate=False)
        self.play_a = Playlist.objects.create(title='Mi playlists', category=cat_a)
        self.cat_a = cat_a
        self.cat_b = cat_b

    def test_is_activate(self):
        self.assertTrue(self.cat_a.activate)

    def test_not_is_activate(self):
        self.assertFalse(self.cat_b.activate)

    def test_related_playlist(self):
        qs = self.cat_a.playlists.all()
        self.assertEqual(qs.count(), 1)


