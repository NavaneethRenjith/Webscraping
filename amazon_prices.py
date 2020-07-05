# Get product details from amazon

import requests
from bs4 import BeautifulSoup


while True:
    url = input("\nEnter url of product : ")
    result = requests.get(url)
    soup = BeautifulSoup(result.content, "html.parser")

    # name of product
    title_tag = soup.find("span", {"id": "productTitle"})
    title = title_tag.string.strip()

    # price of product
    price_tag = soup.find("span", {"id": "priceblock_ourprice"})
    price = price_tag.string

    print(f"\n{title}")
    print(f"\n{price}")

    choice = input("\ndo you wish to continue?(y/n)")
    if choice == "n":
        break

