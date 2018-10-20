from selenium import webdriver
from fixture.group import GroupHelper
from fixture.session_group import SessionHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook")
        return wd

    def destroy(self):
        self.wd.quit()

