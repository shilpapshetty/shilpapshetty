# Read the product URLs from the CSV file
product_urls = []
with open("product_listings.csv", "r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        product_urls.append(row[0])

# Initialize the CSV file for additional product details
csv_file = open("product_details.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Product URL", "Description", "ASIN", "Product Description", "Manufacturer"])

# Scrape details for each product URL
products_to_scrape = 200

for url in product_urls[:products_to_scrape]:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract additional details from the product page
    description = soup.find("meta", attrs={"name": "description"})["content"]
    asin = soup.find("th", string="ASIN").find_next_sibling("td").text.strip()
    product_description = soup.find("div", id="productDescription").text.strip()
    manufacturer = soup.find("th", string="Manufacturer").find_next_sibling("td").text.strip()

    # Write the details to the CSV file
    csv_writer.writerow([url, description, asin, product_description, manufacturer])

csv_file.close()
