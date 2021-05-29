
"""
    Twitter Complaint Bot for Internet Speed

    Measure the current speed and compare is with the advertised speed.
    If current speed less than advertised speed.
    Tweet a complaint to ISP.

"""

from selenium import webdriver
import time

import os
import dotenv
dotenv.load_dotenv()


# CONSTANTS Variables
PROMISED_DOWN = 5
PROMISED_UP = 700
email = os.getenv('EMAIL_TWITTER')
password = os.getenv('PASSWORD_TWITTER')
chrome_driver_path = 'C:/Development/chromedriver.exe'


class TwitterBot:
    """ Initialize Selenium setup, get current internet speed and post tweet """
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_driver_path)  # Initialize web driver
        self.driver.set_window_size(1310, 720)  # Initialize window size
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        """ Get current internet speed and update down and up speeds """
        self.driver.get('https://fast.com/')
        time.sleep(40)  # sleeps for 40 sec to let the test complete
        show_more_info_btn = self.driver.find_element_by_id('show-more-details-link')
        show_more_info_btn.click()
        self.down = int(round(float(self.driver.find_element_by_id('speed-value').text)))  # Get download speed
        self.up = int(round(float(self.driver.find_element_by_id('upload-value').text)))  # Get Upload speed
        self.driver.close()  # Closes the windwon after the test is completed

        if self.down < PROMISED_DOWN and self.up < PROMISED_UP:
            self.post_tweet()

    def post_tweet(self):
        """ Login to twitter and post tweet """
        self.driver.get('https://twitter.com/login')
        time.sleep(2)
        # Get hold of email entry and type in the email
        email_entry = self.driver.find_element_by_name('session[username_or_email]')
        email_entry.send_keys(email)
        # Get hold of password entry and type in the password
        password_entry = self.driver.find_element_by_name('session[password]')
        password_entry.send_keys(password)
        # Grab login button and click it
        login_btn_2 = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span')
        login_btn_2.click()
        time.sleep(5)
        # Go to the tweet section and type in the msg
        tweet_section = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_section.send_keys(
            f"Why I am getting {self.down} Mbps down and {self.up} Kbps up when I am paying for"
            f" 8 Mbps down and 1 Mbps up??? @ptcl.\n"
            f"#Disappointed")
        time.sleep(1)
        # Locate and click tweet button
        tweet_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_btn.click()
        time.sleep(5)
        self.driver.quit()  # Closes the window


tb = TwitterBot()

tb.get_internet_speed()
# tb.post_tweet()

