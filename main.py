import requests
from bs4 import BeautifulSoup


# Get the page
source = requests.get('https://skysmart.ru').text
soup = BeautifulSoup(source, 'html.parser')
# print(soup.prettify())

# Finding useful information
for item in soup.find_all('article', class_='product_pod'):
    title = item.h3.a.text
    price = item.find('p', class_='price_color').text[1:]
    rating = item.p['class'][-1]
    print(title, price, f"Rating: {rating}", sep='\n', end='\n\n')

