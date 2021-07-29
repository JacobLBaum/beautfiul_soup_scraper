from scraper import get_listing_status
from bs4 import BeautifulSoup
import os
import unittest

class scraper_test(unittest.TestCase):

    def test_available_listing1(self):
        script_dir = os.path.dirname(__file__)
        rel_path = r"\html_listings\available_listing1.txt"
        abs_file_path = script_dir + rel_path
        with open(abs_file_path, 'r') as file:
            content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        self.assertEqual(get_listing_status(soup), True,
        'This listing should be listed as available')

    def test_available_listing2(self):
        script_dir = os.path.dirname(__file__)
        rel_path = r"\html_listings\available_listing2.txt"
        abs_file_path = script_dir + rel_path
        with open(abs_file_path, 'r') as file:
            content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        self.assertEqual(get_listing_status(soup), True,
        'This listing should be listed as available')

    def test_available_listing3(self):
        script_dir = os.path.dirname(__file__)
        rel_path = r"\html_listings\available_listing3.txt"
        abs_file_path = script_dir + rel_path
        with open(abs_file_path, 'r') as file:
            content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        self.assertEqual(get_listing_status(soup), True,
        'This listing should be listed as available')

    def test_rented_listing1(self):
        script_dir = os.path.dirname(__file__)
        rel_path = r"\html_listings\rented_listing1.txt"
        abs_file_path = script_dir + rel_path
        with open(abs_file_path, 'r') as file:
            content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        self.assertEqual(get_listing_status(soup), False,
        'This listing should be listed as rented')

    def test_rented_listing2(self):
        script_dir = os.path.dirname(__file__)
        rel_path = r"\html_listings\rented_listing2.txt"
        abs_file_path = script_dir + rel_path
        with open(abs_file_path, 'r') as file:
            content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        self.assertEqual(get_listing_status(soup), False,
        'This listing should be listed as rented')

    def test_rented_listing3(self):
        script_dir = os.path.dirname(__file__)
        rel_path = r"\html_listings\rented_listing3.txt"
        abs_file_path = script_dir + rel_path
        with open(abs_file_path, 'r') as file:
            content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        self.assertEqual(get_listing_status(soup), False,
        'This listing should be listed as rented')

    def test_in_contract_listing1(self):
        script_dir = os.path.dirname(__file__)
        rel_path = r"\html_listings\in_contract_listing1.txt"
        abs_file_path = script_dir + rel_path
        with open(abs_file_path, 'r') as file:
            content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        self.assertEqual(get_listing_status(soup), False,
        'This listing should be listed as in contract')

    def test_in_contract_listing2(self):
        script_dir = os.path.dirname(__file__)
        rel_path = r"\html_listings\in_contract_listing2.txt"
        abs_file_path = script_dir + rel_path
        with open(abs_file_path, 'r') as file:
            content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        self.assertEqual(get_listing_status(soup), False,
        'This listing should be listed as in contract')

    def test_in_contract_listing3(self):
        script_dir = os.path.dirname(__file__)
        rel_path = r"\html_listings\in_contract_listing3.txt"
        abs_file_path = script_dir + rel_path
        with open(abs_file_path, 'r') as file:
            content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        self.assertEqual(get_listing_status(soup), False,
        'This listing should be listed as in contract')

    
if __name__ == '__main__':
    unittest.main()