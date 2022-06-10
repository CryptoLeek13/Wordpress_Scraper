import requests
from bs4 import BeautifulSoup
import csv
import os
# Take url input from user
print("Please Provide a url to be scrapped!")
item_url = input()
# Store the input in r var that uses the requests.get method to retrieve the url
r = requests.get(item_url)
# Once retrieved we pass the data onto bs4 to format the content utilizing lxml processing
soup = BeautifulSoup(r.content, 'lxml')
# we then pass the data onto another var that passes the soup.find_all method searching for all UL's and class
# matching attributes
item_list = soup.findAll('ul', attrs={'class': 'products columns-5'})

product_links = []

for item in item_list:
    for link in item.find_all('a', href=True):
        # print(link['href'])
        product_links.append(link['href'])

        # pass data onto new file in home dir
final_product = product_links
with open("itemList.csv", "w+", newline='') as csvfile:
    data_summary = csv.writer(csvfile)
    data_summary.writerow(final_product)
