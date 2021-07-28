from scraper import listing_status
import unittest

class scraper_test(unittest.TestCase):

    def test_available_listing(self):
        self.assertEqual(listing_status("https://streeteasy.com/building/640-broadway-new_york/5b"), 'Currently available',
        'This listing should be listed as rented or the listing has been updated since the creation of this test')

    def test_rented_listing_1(self):
        self.assertEqual(listing_status("https://streeteasy.com/building/117-mulberry-street-new_york/7"), 'Rented',
        'This listing should be listed as rented or the listing has been updated since the creation of this test')

    def test_rented_listing_2(self):
        self.assertEqual(listing_status("https://streeteasy.com/building/24-st-marks-place-new_york/3"), 'Rented',
        'This listing should be listed as rented or the listing has been updated since the creation of this test')

    def test_rented_listing_3(self):
        self.assertEqual(listing_status("https://streeteasy.com/building/124-mac-dougal-street-new_york/10"), 'Rented',
        'This listing should be listed as rented or the listing has been updated since the creation of this test')
    
    def test_in_contract_listing(self):
        self.assertEqual(listing_status("https://streeteasy.com/building/126-elizabeth-street-new_york/9"), 'In contract',
        'This listing should be listed as rented or the listing has been updated since the creation of this test')
    
if __name__ == '__main__':
    unittest.main()

