# Let's do some testing
from unittest import TestCase

# Generally, with testing you should import code from another file
# but here, we are going to be lazier

class Candidate(object):
    # __init__ initializes the class, allows you to pass arguments into the class
    # at the time you're creating it
    def __init__(self, raw_name, party):
        self.raw_name = raw_name
        self.party = party
        self._parse_name()

    # Private method
    def _parse_name(self):
        name_bits = self.raw_name.split(',')
        self.last_name = name_bits[0].strip() # Strip spaces
        self.first_name = name_bits[1].strip()


# Test-driven development: Write your test before writing the actual class
class TestCandidate(TestCase):

    def test_name_parsing(self):
        cand = Candidate('Smith, John', 'IND')
        # Inheriting behavior assertEqual from TestCase
        # Assert that these two things are equal
        self.assertEqual(cand.last_name, 'Smith') # Real value first, then expected
        self.assertEqual(cand.first_name, 'John')