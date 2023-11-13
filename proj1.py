from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
url = "http://www.google.com"
driver.get(url)
driver.maximize_window()
time.sleep(3)
driver.close()
