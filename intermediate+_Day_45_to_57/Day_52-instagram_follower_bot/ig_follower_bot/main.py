import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os
import dotenv

dotenv.load_dotenv()

email = os.getenv('EMAIL_IG')
password = os.getenv('PASSWORD_IG')

similar_account = ''


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome('C:/Development/chromedriver.exe')
        self.driver.set_window_size(1310, 720)

    def login(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(3)
        email_entry = self.driver.find_element_by_name('username')
        email_entry.send_keys(email)

        password_entry = self.driver.find_element_by_name('password')
        password_entry.send_keys(password)
        password_entry.send_keys(Keys.ENTER)
        time.sleep(5)
        close_popup = self.driver.find_element_by_css_selector('.mt3GC .HoLwm')
        time.sleep(1)
        close_popup.click()

    def find_followers(self):
        pass

    def follow(self):
        pass




# search_bar = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
# search_bar.send_keys('python enthusiast')
# search_bar.send_keys(Keys.ENTER)

