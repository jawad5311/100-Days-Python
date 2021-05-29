
from selenium import webdriver

import os
import dotenv
dotenv.load_dotenv()


# CONSTANTS Variables
PROMISED_DOWN = 5
PROMISED_UP = 1
email = os.getenv('EMAIL_TWITTER')
password = os.getenv('PASSWORD_TWITTER')


chrome_driver_path = 'C:/Development/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path)
driver.set_window_size(1340, 720)



