import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLumaWebsite(unittest.TestCase):

    def setUp(self) -> None:
        url = 'https://magento.softwaretestingboard.com/'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(url)

    def tearDown(self) -> None:
        self.driver.close()

    def test_should_reach_website(self):
        self.assertEqual(self.driver.title, 'Home Page')

        anchors = self.driver.find_elements(By.XPATH, '//ul[@class="header links"]/li/a')
        self.assertEqual('Sign In', anchors[0].text)
        self.assertEqual('Create an Account', anchors[1].text)

    def test_should_visit_register_page_from_homepage(self):
        register_link = self.driver.find_elements(By.XPATH, '//ul[@class="header links"]/li/a')[1]
        register_link.click()
        heading = self.driver.find_element(By.XPATH, '//span[@data-ui-id]')
        self.assertEqual('Create New Customer Account', heading.text)

    def test_should_fail_registration(self):
        register_link = self.driver.find_elements(By.XPATH, '//ul[@class="header links"]/li/a')[1]
        register_link.click()
        self.driver.find_element(By.XPATH, '//button[@title="Create an Account"]').click()
        name_error_div = self.driver.find_element(By.ID, 'firstname-error')
        self.assertEqual('This is a required field.', name_error_div.text)

        mage_error_divs = self.driver.find_elements(By.CSS_SELECTOR, 'div.mage-error')
        self.assertEqual(5, len(mage_error_divs))

    def test_should_register_new_user(self):
        register_link = self.driver.find_elements(By.XPATH, '//ul[@class="header links"]/li/a')[1]
        register_link.click()

        self.driver.find_element(By.ID, 'firstname').send_keys('Vinod')
        self.driver.find_element(By.NAME, 'lastname').send_keys('Kumar')
        self.driver.find_element(By.CSS_SELECTOR, 'input[type=email]#email_address').send_keys('vinod@vinod1234.co')
        self.driver.find_element(By.ID, 'password').send_keys('Welcome#123')
        self.driver.find_element(By.ID, 'password-confirmation').send_keys('Welcome#123')

        self.driver.find_element(By.XPATH, '//button[@title="Create an Account"]').click()

        welcome_message = self.driver.find_element(By.CSS_SELECTOR, 'span.logged-in').text
        self.assertEqual('Welcome, Vinod Kumar!', welcome_message)


