import requests
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

URL = 'https://www.carvana.com/cars/honda-civic-type-r'

opts = Options()
opts.add_argument('--headless')


opts.binary_location_location = os.getcwd() + '.\\chromedriver_win32\chromedriver.exe'
chrome_driver = os.getcwd() + '.\\chromedriver.exe'

driver = webdriver.Chrome()

driver.get(URL)



page = requests.get(URL)
soup_file = driver.page_source
soup = BeautifulSoup(soup_file, 'html.parser')
time.sleep(5)

print("looking for prices")
print(driver.find_elements_by_xpath('//div[@class = "price"]'))


driver.quit()