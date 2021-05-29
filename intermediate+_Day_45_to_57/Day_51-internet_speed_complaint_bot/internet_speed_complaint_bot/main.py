
from selenium import webdriver
import time

import os
import dotenv
dotenv.load_dotenv()


# CONSTANTS Variables
PROMISED_DOWN = 5
PROMISED_UP = 1
email = os.getenv('EMAIL_TWITTER')
password = os.getenv('PASSWORD_TWITTER')
chrome_driver_path = 'C:/Development/chromedriver.exe'


class TwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.set_window_size(1340, 720)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        # self.driver.get('https://fast.com/')
        # time.sleep(60)
        # down_speed = self.driver.find_element_by_id('speed-value')
        # up_speed = self.driver.find_element_by_id('upload-value')
        # # print(down_speed)

    def post_tweet(self):
        pass




