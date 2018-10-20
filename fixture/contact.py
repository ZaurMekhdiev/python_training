from selenium.common.exceptions import NoSuchElementException


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create(self, firstname, middlename, lastname, address, email):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").send_keys(firstname)
        wd.find_element_by_name("middlename").send_keys(middlename)
        wd.find_element_by_name("lastname").send_keys(lastname)
        wd.find_element_by_name("address").send_keys(address)
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_xpath("//input[21]").click()
        self.return_to_home_page()

    def is_element_present(self, how, what):
        try:
            self.app.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True


    def close_alert_and_get_its_text(self):
        try:
            alert = self.app.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

