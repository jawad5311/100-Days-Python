
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chrome_driver_path = 'C:/Development/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path)
driver.set_window_size(1440, 720)

driver.get('http://secure-retreat-92358.herokuapp.com/')

# stats = driver.find_element_by_css_selector('#articlecount a')
# print(stats.text)
#
#
# search = driver.find_element_by_name('search')
# search.send_keys('python')
# search.send_keys(Keys.ENTER)

first_name = driver.find_element_by_name('fName')
last_name = driver.find_element_by_name('lName')
email = driver.find_element_by_name('email')
sign_up = driver.find_element_by_css_selector('.form-signin button')

first_name.send_keys('my first name')
last_name.send_keys('my last name')
email.send_keys('mytestingemail@gmail.com')
sign_up.click()


# driver.close()
