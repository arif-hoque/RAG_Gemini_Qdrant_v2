import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from urllib.parse import urlparse

def scrape_websites(websites, output_folder):
    # Set up Selenium WebDriver
    options = Options()
    options.headless = False  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=options)

    for website in websites:
        print(f"Scraping data from {website}")
        all_urls = get_urls(driver, website)
        print("Total URLs found:", len(all_urls))
        for url in all_urls:
            print("Scraping data from:", url)
            scrape_data_and_save(driver, url, output_folder)

    # Clean up
    driver.quit()

# Function to fetch all URLs from a webpage
def get_urls(driver, base_url):
    driver.get(base_url)
    urls = set()

    # Extract URLs from anchor tags
    for link in driver.find_elements(By.TAG_NAME, 'a'):
        href = link.get_attribute('href')
        if href:
            urls.add(href)

    return urls

# Function to scrape data from a webpage and save it to a text file
def scrape_data_and_save(driver, url, output_folder):
    driver.get(url)
    try:
        # Scraping data
        title = driver.title
        content = driver.find_element(By.TAG_NAME, 'body').text
        
        # Replace unwanted strings with an empty string
        unwanted_strings = [
            "Gigalogy Tutorial",
            "Overview",
            "Account and Project creation",
            "Credentials",
            "Personalizer",
            "Project setup",
            "Environment setup",
            "Integration of Catalogue information and user behavior data",
            "Training your data",
            "Personalized search",
            "Personalized Image Search",
            "Personalized Feed",
            "Recommend trending items",
            "Recommend similar items",
            "Recommend items purchase together",
            "Dynamic Pricing",
            "Questionnaire",
            "MyGPT",
            "API Reference",
            "Release notes",
            "Glossary",
            "HOME PRODUCT",
            "COMPANY",
            "NEWS",
            "CONTACT US",
            "G-Core",
            "SmartAds",
            "Developers",
            "Corporate Profile",
            "Our Mission",
            "Our Team",
            "Careers",
            "PRESS & CONTACT",
            "Request a Demo",
            "Press Room",
            "Events",
            "Experience Box",
            "DEVELOPERS",
            "Partner Program",
            "Recommender - Sandbox",
            "Recommender - Documentation",
            "Recommender - Tutorial",
            "© 2024 Gigalogy Inc. Privacy Policy Terms and Conditions Cookie Policy Commercial Disclosure"
            
        ]

        for string in unwanted_strings:
            content = content.replace(string, "")

        # Remove consecutive empty lines
        content_lines = content.splitlines()
        filtered_content = []
        previous_line_empty = False
        for line in content_lines:
            if line.strip() == "":
                if not previous_line_empty:
                    filtered_content.append(line)
                previous_line_empty = True
            else:
                filtered_content.append(line)
                previous_line_empty = False

        filtered_content_text = "\n".join(filtered_content)

        # Creating the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Writing data to a text file
        filename = os.path.join(output_folder, f"{urlparse(url).netloc}-{urlparse(url).path.replace('/', '_')}.txt")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"URL: {url}\n\n")
            f.write(f"Title: {title}\n\n")
            f.write(f"Content:\n{filtered_content_text}\n")
        print(f"Scraped data saved to {filename}")
    except NoSuchElementException:
        print("Error: Element not found on page", url)

if __name__ == "__main__":
    websites = ["https://gigalogy.com", "https://tutorial.gigalogy.com"]  # Inputted websites
    output_folder = "scraped_data"  # Folder to save the scraped data
    scrape_websites(websites, output_folder)
