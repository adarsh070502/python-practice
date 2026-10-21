from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = Service("C:\Development\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=chrome_driver_path, options=options)

driver.get("https://www.instagram.com/accounts/login/?next=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fonetap%2F%3Fnext%3D%252F%26__coig_login%3D1")
time.sleep(3)

username = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input')
username.click()
username.send_keys("adarsheluri")

password = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input')
password.click()
password.send_keys("8977144405lucky")

submit = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button')
submit.click()
time.sleep(7)

search = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[1]/div')
search.click()

time.sleep(2)
search_bar = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
search_bar.send_keys("talkfootballhd")

time.sleep(3)

totalfootball = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div')
totalfootball.click()

time.sleep(7)

followers = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
followers.click()
time.sleep(3)

div_element = driver.find_element(By.CSS_SELECTOR, 'div._aano')
for _ in range(5):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", div_element)
    time.sleep(2)
    buttons = driver.find_elements(By.CLASS_NAME, "_acan._acap._acas._aj1-")

    print(f"Found {len(buttons)} buttons")
    time.sleep(2)

    for button in buttons:
        button.click()
        time.sleep(1)

