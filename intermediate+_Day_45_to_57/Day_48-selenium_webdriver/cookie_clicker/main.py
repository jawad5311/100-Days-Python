
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

timeout = time.time() + 1

while True:
    cookie.click()
    if time.time() > timeout:
        # timeout = time.time() + 5
        # print('Timed Out')
        # grayed = driver.find_element_by_class_name('grayed')
        # item = EC.invisibility_of_element(grayed)

        all_prices = driver.find_elements_by_css_selector("#store b")

        item_prices = []

        for price in all_prices[:-1]:
            item_price = price.text.split(' ')[-1]
            try:
                item_price = int(item_price)
            # print(item_price)
            except ValueError:
                item_price = int(item_price.replace(',', ''))
            finally:
                item_prices.append(item_price)

        print(item_prices)


        driver.close()
        break





