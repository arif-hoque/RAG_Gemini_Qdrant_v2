import time
from selenium import webdriver
from parsel import Selector
import json
import re
import os

def scrape_api_documentation(redoc_url):
    # Set up Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=options)

    # Navigate to the Redoc website
    driver.get(redoc_url)
    print(f"Navigating to {redoc_url}")
    time.sleep(5)  # Wait for the page to load
    redoc_html = driver.page_source

    # Save the Redoc page source to a text file in the same directory
    output_file_path = os.path.join(os.path.dirname(__file__), 'redoc_page_source2.txt')
    with open(output_file_path, 'w', encoding='utf-8') as redoc_file:
        redoc_file.write(redoc_html)

    print(f"Redoc page source saved to {output_file_path}")

    driver.quit()

if __name__ == "__main__":
    redoc_url = 'https://api.recommender.gigalogy.com/redoc'
    scrape_api_documentation(redoc_url)
