# Amazon Product Scraper
This repository contains Python code to scrape product information from Amazon search result pages using Selenium and BeautifulSoup. The code demonstrates how to load a webpage, extract specific information, and store it in a pandas DataFrame.

## Dependencies
- selenium
- beautifulsoup4
- pandas

You can install the required packages using pip:
- pip install selenium beautifulsoup4 pandas

## Setup
You will need to download the appropriate ChromeDriver for your system from the following link:
- ChromeDriver Download

Place the downloaded chromedriver in the same directory as the script, or update the path in the script accordingly.

## Code Structure
The code is structured in the following way:
- scrape_amazon_products(url): A function that takes a URL as its argument, loads the webpage using Selenium, and extracts product information (name, price, and rating) using BeautifulSoup. It returns a pandas DataFrame containing the scraped data.

## Usage
To use the code, you can run the script amazon_scraper.py:
- python amazon_scraper.py

This script will:
- Call the scrape_amazon_products(url) function with a predefined Amazon search result URL.
- Store the scraped product information in a pandas DataFrame.
- Save the DataFrame as a CSV file.

## Customization
You can customize the code by updating the URL or modifying the scraping logic within the scrape_amazon_products() function to fit your specific requirements.
