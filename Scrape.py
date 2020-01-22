from bs4 import BeautifulSoup
import requests
import csv

#Enter a nike product page to
source = requests.get('https://www.nike.com/w/men-basketball-shoes-3glsmznik1zy7ok').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('Nike_Product_Scraper.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product', 'Price'])

#https://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20?rq=1
#print(soup.prettify().encode('utf-8'))

for data in soup.find_all('div',class_='grid-item-box'):
    product_name = data.find('div',class_='product-name').p.text
    print(product_name)

    product_price = data.find('span',class_='local').text
    print(product_price)

    csv_writer.writerow([product_name,product_price])

csv_file.close()
