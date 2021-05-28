
from selenium import webdriver

chrome_driver_path = 'C:/Development/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path)
driver.set_window_size(1440, 720)
# driver.get('https://www.amazon.com/ELECJET-PowerPie-20000mAh-External-Nintendo/dp/B07YLFX8DT/ref=sr_1_2_sspa?dchild=1&keywords=laptop+power+bank&qid=1622188568&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExRldKRUI5WkU4STM5JmVuY3J5cHRlZElkPUEwODA1MzY2MUgwV0tQV0RBOEQzUiZlbmNyeXB0ZWRBZElkPUEwNDQ4MTg5MU0zRkpBNDMxVVpVRCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=')
# price = driver.find_element_by_id('priceblock_ourprice')
# print(price.text)


driver.get('https://www.python.org/')

date = driver.find_elements_by_css_selector('.event-widget time')
# print(type(date))
# print(date)

title = driver.find_elements_by_css_selector('.event-widget ul a')

# for _ in title:
#     print(_.text)
#
# for _ in date:
#     print(_.text)

data = {}

for index in range(len(date)):
    data[str(index)] = {'name': title[index].text, 'date': date[index].text}

print(data)


driver.close()
