from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
# url = "https://www.baidu.com/"
# value = "kw"
# url = "https://www.google.com/"
# value = "ApjFqb"
url = "https://hk.yahoo.com/"
value = "p"
driver.get(url)
driver.maximize_window()
search = driver.find_element(By.NAME, value)
search.send_keys('erb')
search.send_keys(Keys.ENTER)
time.sleep(300)
search.clear()
driver.close()
