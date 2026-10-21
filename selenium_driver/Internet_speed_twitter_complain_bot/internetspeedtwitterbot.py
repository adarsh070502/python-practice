import os
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = Service("C:\Development\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=chrome_driver_path, options=options)


class InternetSpeedTwitterBot:

    def __init__(self):
        self.promised_speed = 50
        self.twitter_username = "@eluriadarsh"
        self.twitter_password = os.environ.get("TWITTER_PASSWORD")

    def net_speed_bot(self):
        driver.get("https://www.speedtest.net/")
        time.sleep(3)

        button = driver.find_element(By.XPATH,
                                     '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        print("buttun clicked")
        button.click()
        time.sleep(45)
        download_speed = float(driver.find_element(By.XPATH,
                                                   '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        print(download_speed)
        return download_speed

    def twitter_bot(self, download_speed):
        time.sleep(5)
        driver.get("https://twitter.com/home")
        time.sleep(5)

        username = driver.find_element(By.CSS_SELECTOR, 'label.css-1dbjc4n.r-1roi411.r-z2wwpe.r-rs99b7.r-18u37iz')
        username.send_keys(self.twitter_username)

        next1 = driver.find_element(By.CLASS_NAME,
                                    'css-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-ywje51.r-usiww2.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr.r-13qz1uu')
        next1.click()

        time.sleep(5)

        password = driver.find_element(By.CLASS_NAME,
                                       "r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu")
        password.send_keys(self.twitter_password)

        login = driver.find_element(By.XPATH,
                                    '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        login.click()

        time.sleep(5)

        post1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        post1.click()
        time.sleep(2)

        text = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div')
        text.send_keys(f"@ACTFibernet you promised us 25 per sec, but i am getting only {download_speed} per sec")

        time.sleep(2)
        post2 = driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]')
        post2.click()
