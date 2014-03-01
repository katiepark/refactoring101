# Let's do some testing
from unittest import TestCase

# Generally, with testing you should import code from another file
# but here, we are going to be lazier

class Cat(object):

    def sound(self):
        return 'meow'

class TestCat(TestCase):

    def test_sound(self):
        cat = Cat()
        # Inheriting behavior assertEqual from TestCase
        # Assert that these two things are equal
        self.assertEqual(cat.sound(), 'mrow') # Real value first, then expected