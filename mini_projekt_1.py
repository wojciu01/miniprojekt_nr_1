#! /usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

valid_job = 'QA'
valid_city = 'Przemyśl'

class OLXsearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.olx.pl/")

    def test_tytul(self):
        title = self.driver.title
        print(title)
        assert title == 'Ogłoszenia - Sprzedam, kupię na OLX.pl'

    def test_search_job(self):
        choose_job = self.driver.find_element_by_xpath('//a[@data-id="4" and @class="link parent   "]')
        choose_job.click()
        job = self.driver.find_element_by_xpath('//input[@id="headerSearch"]')
        job.send_keys(valid_job)
        city = self.driver.find_element_by_xpath('//input[@id="cityField"]')
        city.send_keys(valid_city)
        search = self.driver.find_element_by_xpath('//input[@type="submit"]')
        search.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)