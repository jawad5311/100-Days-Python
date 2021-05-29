
from selenium import webdriver
import time

import os
import dotenv
dotenv.load_dotenv()


# CONSTANTS Variables
PROMISED_DOWN = 5
PROMISED_UP = 70
email = os.getenv('EMAIL_TWITTER')
password = os.getenv('PASSWORD_TWITTER')
chrome_driver_path = 'C:/Development/chromedriver.exe'


class TwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.set_window_size(1310, 720)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get('https://fast.com/')

        time.sleep(40)

        show_more_info_btn = self.driver.find_element_by_id('show-more-details-link')
        show_more_info_btn.click()

        self.down = int(round(float(self.driver.find_element_by_id('speed-value').text)))
        self.up = int(round(float(self.driver.find_element_by_id('upload-value').text)))

        self.driver.close()

        # print(down_speed)
        # print(up_speed)

    def post_tweet(self):
        # print(self.down)
        # print(self.up)

        self.driver.get('https://twitter.com/?lang=en')
        login_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div/span/span')
        time.sleep(3)
        login_btn.click()

        time.sleep(1)

        email_col = self.driver.find_element_by_name('session[username_or_email]')
        email_col.send_keys(email)

        password_col = self.driver.find_element_by_name('session[password]')
        password_col.send_keys(password)

        login_btn_2 = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span')
        login_btn_2.click()

        time.sleep(5)

        tweet_section = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_section.send_keys('Good Evening everyone! \nTell me something '
                                'better than an evening chai\n#chai ')
        # self.driver.close()
        time.sleep(10)
        tweet_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_btn.click()
        time.sleep(5)



tb = TwitterBot()

# tb.get_internet_speed()
tb.post_tweet()

