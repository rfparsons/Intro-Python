import unittest
from supplier_library import suppliers

# WARNING: These tests could fail if names/prices of items change!
# If they end up failing, make sure they line up with the information on the website

class ExceptionTests(unittest.TestCase):
    def setUp(self):
        self.andymark_part = suppliers.andymark_item("am-3000")
        self.rev_part = suppliers.rev_item("rev-21-1650")

    def tearDown(self):
        del self.andymark_part
        del self.rev_part

    def test_am_price_valid(self):
        self.assertEquals(self.andymark_part.get_price(), 435.0)

    def test_rev_price_valid(self):
        self.assertEquals(self.rev_part.get_price(), 40.0)

    def test_am_name_valid(self):
        self.assertEquals(self.andymark_part.get_name(), "NI roboRIO")

    def test_rev_name_valid(self):
        self.assertEquals(self.rev_part.get_name(), "NEO Brushless Motor")

    def test_am_url_valid(self):
        self.assertEquals(self.andymark_part.get_url(), "https://www.andymark.com/am-3000")

    def test_rev_url_valid(self):
        self.assertEquals(self.rev_part.get_url(), 'https://www.revrobotics.com/rev-21-1650')

    def test_invalid_am_part(self):
        with self.assertRaises(suppliers.ItemNotFoundException):
            suppliers.andymark_item("am-0000")
    
    def test_invalid_rev_part(self):
        with self.assertRaises(suppliers.ItemNotFoundException):
            suppliers.rev_item("rev-00-0000")

if __name__ == '__main__':
    unittest.main()