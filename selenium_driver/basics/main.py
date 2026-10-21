from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:\Development/chromedriver.exe"

service = Service(executable_path='./chromedriver.exe')
driver = webdriver.Chrome()

driver.get("https://www.python.org/")
'''price = driver.find_element(By.NAME, "q")
print(price.tag_name)
print(price.get_attribute("placeholder"))'''

'''logo = driver.find_element(By.CLASS_NAME,"python-logo")
print(logo.size)'''

'''docs_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(docs_link.text)'''

'''element = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(element.text)'''

'''driver.get("https://www.vijaysales.com/apple-iphone-14-128-gb-starlight/21976")
price = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_fillprice"]/div/span[2]/span')
print(price.text)'''

time.sleep(3)

'''upcoming_event = driver.find_element(By.XPATH,'/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li[2]/a')
print(upcoming_event.text)'''

'''upcoming_events = driver.find_elements(By.XPATH,'//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
for u in upcoming_events:
    data = u.text.encode("utf-8","ignore")

data1 = str(data, 'UTF-8')

for d in data1:
    if(d==" "):
        print("")
    else:
        print(d,end="")'''

times = driver.find_elements(By.CSS_SELECTOR,".event-widget time")
events_py = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")


events={}
for i in range(len(events_py)):
    events[i]={
        "time":times[i].text,
        "event":events_py[i].text
    }

print(events)

