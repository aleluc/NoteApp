from django.test import TestCase
from selenium import webdriver

from .forms import AddForm

class FunctionalTestCase(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_homepage_exists(self):
        # when
        self.browser.get('http://localhost:8000')

        # then
        self.assertIn('All notes', self.browser.page_source)

    def test_add_note(self):
        # given
        self.browser.get('http://localhost:8000')

        # when
        self.browser.find_element_by_name('Add Note').click()
        title = self.browser.find_element_by_id('id_title')
        title.send_keys('Test note')
        content = self.browser.find_element_by_id('id_content')
        content.send_keys('Test content')
        self.browser.find_element_by_name('submit').click()

        # then
        self.browser.find_element_by_name('Test note').click()
        self.assertIn('Test content', self.browser.page_source)

    # def test_remove_note(self):
    #     pass

    # def test_edit_note(self):
    #     pass

    # def test_share_note(self):
    #     pass

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

class UnitTestCase(TestCase):

    def test_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_add_form(self):
        form = AddForm(data={
            'title': 'Test note',
            'content': 'Test content',
        })
        self.assertTrue(form.is_valid())
