from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

def scrape_amazon_products(url):
    # Creating a webdriver instance
    driver = webdriver.Chrome("./chromedriver")

    # Opening the URL in the browser using the driver
    driver.get(url)

    # Get the HTML content from the page
    html_content = driver.page_source

    # Close the webdriver instance
    driver.quit()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all products on the page
    products = soup.find_all('div', {'class': 's-result-item'})

    # Initialize empty lists to store the scraped data
    names = []
    prices = []
    ratings = []

    # Loop through each product and extract the name, price, and rating
    for product in products:
        # Extract the name of the product
        name_element = product.find('h2', {'class': 'a-size-mini'})
        if name_element:
            name = name_element.text.strip()
        else:
            name = "N/A"
        names.append(name)

        # Extract the price of the product
        price_element = product.find('span', {'class': 'a-price-whole'})
        if price_element:
            price = price_element.text.strip()
        else:
            price = "N/A"
        prices.append(price)

        # Extract the rating of the product
        rating_element = product.find('span', {'class': 'a-icon-alt'})
        if rating_element:
            rating = rating_element.text.strip()
        else:
            rating = "N/A"
        ratings.append(rating)

    # Create a DataFrame from the scraped data
    df = pd.DataFrame({
        'Name': names,
        'Price (£)': prices,
        'Rating': ratings
    })

    return df

if __name__ == "__main__":
    url = "https://www.amazon.co.uk/s?k=computers&crid=2MH77T8FMGIFK&sprefix=computer%2Caps%2C133&ref=nb_sb_noss_1"
    df = scrape_amazon_products(url)
    
    # Save the DataFrame as a CSV file
    df.to_csv('./amazon_computers_uk.csv', index=False)

    # Display the DataFrame
    print(df)
