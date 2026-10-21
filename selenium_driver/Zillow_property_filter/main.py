import requests
from bs4 import BeautifulSoup

docs_link = "https://docs.google.com/forms/d/e/1FAIpQLSc_-waVm17P41L3O1T95KTBhkSxfD-FUOHtszDeGK0QQjHjNA/viewform?usp=sf_link"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(
    url="https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C"
        "%22mapBounds%22%3A%7B%22north%22%3A38.02766618246823%2C%22east%22%3A-121.90323866796875%2C%22south%22%3A37"
        ".71382801803018%2C%22west%22%3A-122.44294203710938%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330"
        "%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max"
        "%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B"
        "%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr"
        "%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22"
        "%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D",
    headers=header)

soup = BeautifulSoup(response.text, "html.parser")
prices_response = soup.select(".PropertyCardWrapper__StyledPriceGridContainer-srp__sc-16e8gqd-0 kSsByo a")
all_prices = []

for price in prices_response:
    print(price.text)


