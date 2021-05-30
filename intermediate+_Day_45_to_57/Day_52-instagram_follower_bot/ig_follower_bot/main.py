import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os
import dotenv

dotenv.load_dotenv()  # Loads Environment variables

# Insta email and password
email = os.getenv('EMAIL_IG')
password = os.getenv('PASSWORD_IG')

insta_url = 'https://www.instagram.com/'
similar_account = 'follovv_for_follovv'  # insta user whom followers bot will follow


class InstaFollower:
    """
    Insta follower bot.
        Login to insta,
        Find followers,
        Follow them,
        Logout.
    """
    def __init__(self):
        """ Initialize Selenium Web Driver """
        self.driver = webdriver.Chrome('C:/Development/chromedriver.exe')
        self.driver.set_window_size(1310, 720)

    def login_insta(self):
        """ Login to Insta """
        self.driver.get(insta_url)
        time.sleep(3)

        # Get hold of email and password entries
        email_entry = self.driver.find_element_by_name('username')
        password_entry = self.driver.find_element_by_name('password')

        # Type in email & password and press Enter key
        email_entry.send_keys(email)
        password_entry.send_keys(password)
        password_entry.send_keys(Keys.ENTER)
        time.sleep(5)

        # Close the Notification Popup
        close_popup = self.driver.find_element_by_css_selector('.mt3GC .HoLwm')
        close_popup.click()

    def find_followers(self):
        """ Find the followers of the account you want to follow """
        self.driver.get(f"{insta_url}{similar_account}")
        time.sleep(5)
        # Find the followers button and click it
        followers_popup = self.driver.find_element_by_css_selector('header a')
        followers_popup.click()
        # print(followers_popup.text)
        time.sleep(2)
        # Holds the div in which the followers are appearing
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')

        for i in range(3):
            """ Scroll down the followers list """
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(1)

    def follow(self):
        """ Follows the find users """
        # Locate the follow buttons of the all the users in followers list
        follow_btns = self.driver.find_elements_by_css_selector('.PZuss button')
        # Go through each button and if button text is follow then click on it
        for btn in follow_btns:
            if btn.text == 'Follow':
                time.sleep(1)
                btn.click()
                rand_time = random.randint(2, 40)  # Creates a random int to be use as time
                print(rand_time)
                time.sleep(rand_time)  # wait for the time until click on the next button

    def logout_insta(self):
        """ Logout user from the insta """
        # Find profile img and click on it
        profile_img = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img')
        profile_img.click()
        time.sleep(1)
        # Find logout from the drop down menu and click it
        log_out = self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div')
        log_out.click()


bot = InstaFollower()
bot.login_insta()
bot.find_followers()
bot.follow()


