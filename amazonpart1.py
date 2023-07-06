import requests
from bs4 import BeautifulSoup
import csv

# Part 1: Scrape
base_url = "https://www.amazon.in/s"
search_query = "bags"

# Scrape 20 pages of product listings
pages_to_scrape = 20

# Initialize the CSV file
csv_file = open("product_listings.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Product URL", "Product Name", "Product Rating", "Number of Reviews"])

for page in range(1, pages_to_scrape + 1):
    params = {
        "k": search_query,
        "page": page
    }
    response = requests.get(base_url, params=params)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all the product listings on the page
    product_listings = soup.find_all("div", class_="sg-col-inner")

    # Extract information from each product listing
    for listing in product_listings:
        # Extract the product URL
        product_url = listing.find("a", class_="a-link-normal s-no-outline")["href"]

        # Extract the product name
        product_name = listing.find("span", class_="a-size-base-plus a-color-base a-text-normal").text.strip()

        # Extract the product rating
        rating_element = listing.find("span", class_="a-icon-alt")
        product_rating = rating_element.text.strip() if rating_element else "N/A"

        # Extract the number of reviews
        review_element = listing.find("span", class_="a-size-base")
        num_reviews = review_element.text.strip().replace(",", "") if review_element else "0"

        # Write the information to the CSV file
        csv_writer.writerow([product_url, product_name, product_rating, num_reviews])

csv_file.close()
