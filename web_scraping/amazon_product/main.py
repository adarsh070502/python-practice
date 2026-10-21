import requests
from bs4 import BeautifulSoup
import lxml
from mail_sender import Mail

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(url="https://www.amazon.in/Apple-iPhone-14-128GB-Blue/dp/B0BDK62PDX/ref=sr_1_1_sspa?crid"
                            "=1YBCBTYQCWP6Y&keywords=iphone+14&qid=1692897073&sprefix=iphon%2Caps%2C236&sr=8-1-spons"
                            "&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1", headers=headers)


soup = BeautifulSoup(response.content, "lxml")
#print(soup.prettify().encode("utf-8"))
price_str = soup.find(name="span", class_="a-price-whole").text
price = int(price_str[:len(price_str)-1].replace(",",""))

if price<70000:
    mail = Mail()
    message = f"Iphone is available {price} less than 70,000"
    mail.send_mail(message)

