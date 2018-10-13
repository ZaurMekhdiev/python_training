# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from contact import Contact



class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.open_home_page()
        self.login(wd, username="admin", password="secret")
        self.create_contact(wd, firstname="test1", middlename="test2", lastname="test3", address="test4", email="test5")
        self.return_to_home_page(wd)
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.open_home_page()
        self.login(wd, username="admin", password="secret")
        self.create_contact(wd, firstname="", middlename="", lastname="", address="", email="")
        self.return_to_home_page(wd)
        self.logout(wd)

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, wd, firstname, middlename, lastname, address, email):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").send_keys(firstname)
        wd.find_element_by_name("middlename").send_keys(middlename)
        wd.find_element_by_name("lastname").send_keys(lastname)
        wd.find_element_by_name("address").send_keys(address)
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_xpath("//input[21]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")
        return wd

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()



