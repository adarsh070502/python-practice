from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = Service("C:\Development\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=chrome_driver_path, options=options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
time.sleep(2)

cookie_button = driver.find_element(By.ID, "cookie")

click_button = driver.find_element(By.ID, "buyCursor")

time1 = time.time() + 60 * 5
ten_seconds = time.time() + 5
while True:
    if time.time() > time1:
        break

    cookie_button.click()

    if time.time() > ten_seconds:
        money = int(driver.find_element(By.ID,"money").text)
        all_prices1 = driver.find_elements(By.CSS_SELECTOR, "#store b")
        all_prices = [all_prices1[i].text.split()[2] for i in range(len(all_prices1)-1,-1,-1)]
        all_buttons = driver.find_elements(By.CSS_SELECTOR, "store id")

        for i in range(len(all_prices)):
            if money > int(all_prices[i]):
                all_buttons[i].click()
        time1 = time.time()+5


