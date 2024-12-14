import requests
import pandas as pd
from bs4 import BeautifulSoup
from lxml import html
import openpyxl
import os


url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

names = soup.find_all("a", class_ = "title")


product_name = []


for i in names:
    name = i.text
    product_name.append(name)


prices = soup.find_all("h4", class_ = "price float-end card-title pull-right")


prices_list = []


for i in prices:
    price = i.text
    prices_list.append(price)


desc = soup.find_all("p", class_ = "description card-text")

desc_list = []

for i in desc:
    desc = i.text
    desc_list.append(desc)


reviews = soup.find_all("p", class_ = "review-count float-end")

reviews_list = []

for i in reviews:
    rew = i.text
    reviews_list.append(rew)

df = pd.DataFrame({
    "Product Name": product_name,
    "Prices" : prices_list,
    "Description" : desc_list,
    "Number of Reviews" : reviews_list
})

products_details = 'products_details.xlsx'

df.to_excel(products_details, index=False, engine='openpyxl') 
#print(df)

print(f"DataFrame successfully saved to {products_details}")


# Open the Excel file automatically (Windows-specific)
os.system(f'start excel "{products_details}"')