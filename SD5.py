import requests
from bs4 import BeautifulSoup
import pandas as pd

# Replace with the actual URL of the e-commerce site
url = "https://www.example.com/category/products"

# Send a request to fetch the HTML content
try:
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
except requests.exceptions.HTTPError as errh:
    print ("Http Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print ("OOps: Something Else", err)

soup = BeautifulSoup(response.content, 'html.parser')

# Lists to store the scraped data
product_names = []
product_prices = []
product_ratings = []

# Example selectors - these will vary depending on the actual site structure
for product in soup.find_all('div', class_='product-item'):
    name = product.find('h2', class_='product-title').text.strip()
    price = product.find('span', class_='product-price').text.strip()
    rating = product.find('div', class_='product-rating').text.strip()
    
    product_names.append(name)
    product_prices.append(price)
    product_ratings.append(rating)

# Create a DataFrame from the lists
data = {
    'Product Name': product_names,
    'Price': product_prices,
    'Rating': product_ratings
}

df = pd.DataFrame(data)

# Save the data to a CSV file
df.to_csv('products.csv', index=False)

print("Data has been successfully scraped and saved to 'products.csv'.")
