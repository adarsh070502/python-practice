from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


chrome_driver_path = "C:\\Development\\chromedriver.exe"

driver = webdriver.Chrome()

driver.get("https://en.wikipedia.org/wiki/Main_Page")

time.sleep(2)
'''num = driver.find_element(By.CSS_SELECTOR, "#articlecount a").text
print(num)'''

'''link = driver.find_element(By.LINK_TEXT, "View history")
time.sleep(3)
link.click()
time.sleep(3)'''

search = driver.find_element(By.CLASS_NAME,"cdx-text-input__input")
search.send_keys("python")
search.send_keys(Keys.ENTER)
time.sleep(10)


driver.close()
