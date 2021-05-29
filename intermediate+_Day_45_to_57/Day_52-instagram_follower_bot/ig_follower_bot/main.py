import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os
import dotenv

dotenv.load_dotenv()

email = os.getenv('EMAIL_IG')
password = os.getenv('PASSWORD_IG')


driver = webdriver.Chrome('C:/Development/chromedriver.exe')
driver.set_window_size(1310, 720)

driver.get('https://www.instagram.com/')
time.sleep(5)
email_entry = driver.find_element_by_name('username')
email_entry.send_keys(email)
email_entry.send_keys(Keys.ENTER)

password_entry = driver.find_element_by_name('password')
password_entry.send_keys(password)
password_entry.send_keys(Keys.ENTER)




