import unittest

from selenium import webdriver




class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

# ==================================================================================================