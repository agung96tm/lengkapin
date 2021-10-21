from django.test import TestCase


class Hello(TestCase):
    def test_say_hi(self):
        self.assertEqual('hi', 'hi')
