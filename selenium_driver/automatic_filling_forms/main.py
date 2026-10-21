from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://secure-retreat-92358.herokuapp.com/")
time.sleep(3)

fname = driver.find_element(By.NAME,"fName")
fname.send_keys("ELURI")

time.sleep(3)

lname = driver.find_element(By.NAME,"lName")
lname.send_keys("ADARSH")

time.sleep(3)

email = driver.find_element(By.NAME,"email")
email.send_keys("adarsheluri143@gmail.com")

time.sleep(3)

submit = driver.find_element(By.CSS_SELECTOR,'form button')
submit.send_keys(Keys.ENTER)
