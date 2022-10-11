from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    """Docstring for NewVisitorTest. """

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new onlihne to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She types "Buy a peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some 
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.browser
        # Satisfied, she goes back to sleep

if __name__ == "__main__":
    unittest.main()
