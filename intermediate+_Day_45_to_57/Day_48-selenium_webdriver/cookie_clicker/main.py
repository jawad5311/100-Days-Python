
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

import time


chrome_driver_path = 'C:/Development/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path)
driver.set_window_size(1440, 720)

driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element_by_id('cookie')


# cookie_count = int(driver.find_element_by_id('money').text)
# print(type(cookie_count))
# print(cookie_count)


items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]
# print(item_ids)


timeout = time.time() + 20
five_min = time.time() + 60


while True:

    cookie.click()

    if time.time() > timeout:
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

        cookie_upgrades = {}

        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # print(cookie_upgrades)

        cookie_count = driver.find_element_by_id('money').text
        try:
            cookie_count = int(cookie_count)
        except ValueError:
            cookie_count = int(cookie_count.replace(',', ''))

        # print(cookie_count)
        # print(type(cookie_count))

        affordable_upgrades = {}

        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # print(affordable_upgrades)

        highest_price_affordable_upgrade = max(affordable_upgrades)
        # print(highest_price_affordable_upgrade)

        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        print(to_purchase_id)

        driver.find_element_by_id(to_purchase_id).click()

        timeout = time.time() + 5

        if time.time() > five_min:
            cookie_per_s = driver.find_element_by_id("cps").text
            five_min = time.time() + 60
            print(cookie_per_s)

        # driver.close()
        # break





