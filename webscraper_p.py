import requests
import pandas as pd
from bs4 import BeautifulSoup
from lxml import html


url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

r = requests.get(url)

#print(r)
soup = BeautifulSoup(r.text, "lxml")

names = soup.find_all("a", class_ = "title")

#print(names)

product_name = []


for i in names:
    name = i.text
    product_name.append(name)

#print(product_name)

prices = soup.find_all("h4", class_ = "price float-end card-title pull-right")
#print(prices)


prices_list = []


for i in prices:
    price = i.text
    prices_list.append(price)

#print(prices_list)

desc = soup.find_all("p", class_ = "description card-text")
#print(desc)

desc_list = []


for i in desc:
    desc = i.text
    desc_list.append(desc)

#print(desc_list)

reviews = soup.find_all("p", class_ = "review-count float-end")
#print(reviews)


reviews_list = []


for i in reviews:
    rew = i.text
    reviews_list.append(rew)

#print(reviews_list)


df = pd.DataFrame({
    "Product Name": product_name,
    "Prices" : prices_list,
    "Description" : desc_list,
    "Number of Reviews" : reviews_list
})

#print(df)


df.to_csv("products_details.csv")
