from django.test import TestCase
from selenium import webdriver

from .forms import AddNoteForm

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
        title.send_keys('Test')
        content = self.browser.find_element_by_id('id_content')
        content.send_keys('Test content')
        self.browser.find_element_by_name('submit').click()

        # then
        self.assertIn('Test content', self.browser.page_source)
        self.browser.find_element_by_name('remove').click()

    def test_remove_note(self):
        #given
        self.browser.get('http://localhost:8000')
        self.browser.find_element_by_name('Add Note').click()
        title = self.browser.find_element_by_id('id_title')
        title.send_keys('Remove_test')
        content = self.browser.find_element_by_id('id_content')
        content.send_keys('Test content')
        self.browser.find_element_by_name('submit').click()

        # when
        self.browser.find_element_by_name('remove').click()

        # then
        self.assertNotIn('Remove_test', self.browser.page_source)

    def test_edit_note(self):
        #given
        self.browser.get('http://localhost:8000')
        self.browser.find_element_by_name('Add Note').click()
        title = self.browser.find_element_by_id('id_title')
        title.send_keys('Edit_test')
        content = self.browser.find_element_by_id('id_content')
        content.send_keys('Test content')
        self.browser.find_element_by_name('submit').click()

        # when
        self.browser.find_element_by_name('edit').click()
        title = self.browser.find_element_by_id('id_title')
        title.send_keys('Edit_test_edited')
        content = self.browser.find_element_by_id('id_content')
        content.send_keys('Test content edited')
        self.browser.find_element_by_name('save').click()

        # then
        self.assertIn('Edit_test_edited', self.browser.page_source)
        self.assertIn('Test content edited', self.browser.page_source)

    # def test_share_note(self):
    #     pass

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

class UnitTestCase(TestCase):

    def test_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_note_detail_page_template(self):
        pass

    def test_add_note_page_template(self):
        pass

    def test_remove_note_page_template(self):
        pass

    def test_add_form(self):
        form = AddNoteForm(data={
            'title': 'Test note',
            'content': 'Test content',
        })
        self.assertTrue(form.is_valid())
