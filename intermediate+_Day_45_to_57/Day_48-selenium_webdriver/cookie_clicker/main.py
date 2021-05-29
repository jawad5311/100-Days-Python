
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

import time


chrome_driver_path = 'C:/Development/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path)
driver.set_window_size(1440, 720)

driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element_by_id('cookie')
cookie.click()
cookie.click()
cookie.click()
cookie.click()
cookie.click()
cookie.click()
cookie.click()


cookie_count = int(driver.find_element_by_id('money').text)
print(type(cookie_count))
print(cookie_count)

# buy_cursor = driver.find_element_by_id('buyCursor').text
# print(buy_cursor)

# store = driver.find_element_by_id('store')
# print(store.text)

# check = driver.find_element_by_css_selector('#buyCursor .grayed').text
# print(check)

# EC.invisibility_of_element()

# condition = cookie_count *

timeout = time.time() + 10

while cookie_count < 1000:
    cookie.click()
    if time.time() > timeout:
        timeout = time.time() + 5
        print('Timed Out')
        # grayed = driver.find_element_by_class_name('grayed')
        # item = EC.invisibility_of_element(grayed)






