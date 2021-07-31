from django.test import TestCase
from selenium import webdriver

class FunctionalTestCase(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_homepage_exists(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('All notes', self.browser.page_source)

    def test_add_note(self):
        pass

    def test_remove_note(self):
        pass

    def test_edit_note(self):
        pass

    def test_share_note(self):
        pass

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

class UnitTestCase(TestCase):
    pass