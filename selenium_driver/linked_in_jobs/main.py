from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = Service("C:\Development\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=chrome_driver_path, options=options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3700249830&f_AL=true&f_E=1%2C2&keywords=python%20developer&refresh=true")
sign_in = driver.find_element(By.CSS_SELECTOR," .conversion-modal a")
time.sleep(2)
sign_in.click()

time.sleep(2)

username_input = driver.find_element(By.ID,"username")
username_input.send_keys("adarsheluri143@gmail.com")
password_input = driver.find_element(By.ID,"password")
password_input.send_keys("8977144405adarsh")
#time.sleep(2)
sign_in_1 = driver.find_element(By.CSS_SELECTOR,".login__form_action_container button")
sign_in_1.click()

time.sleep(2)

done_button = driver.find_element(By.CSS_SELECTOR,".jobs-apply-button--top-card button")
done_button.click()

time.sleep(2)

phonenumber = driver.find_element(By.CSS_SELECTOR,".ember-view input")
phonenumber.send_keys("7569562436")

time.sleep(2)

next1 = driver.find_element(By.CSS_SELECTOR,".ph5 button")
next1.click()

time.sleep(1)

next2 = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]')
next2.click()

years_expierence = driver.find_element(By.CSS_SELECTOR,".ember-view input")
years_expierence.send_keys("2")

city_option = driver.find_element(By.XPATH,'//*[@id="text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3700249830-96396594-multipleChoice"]')
city_option.click()

Yes_option = driver.find_element(By.XPATH,'//*[@id="text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3700249830-96396594-multipleChoice"]/option[2]')
Yes_option.click()

django = driver.find_element(By.XPATH,'//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3700249830-96396586-numeric"]')
django.send_keys("1")

review = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]')
review.click()

submit = driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]")
submit.click()



