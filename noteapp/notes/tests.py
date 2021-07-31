from django.test import TestCase
from selenium import webdriver

class FunctionalTestCase(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_homepage_exists(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('All notes', self.browser.page_source)

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

class UnitTestCase(TestCase):
    pass