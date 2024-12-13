# Web Scraping E-commerce Product Details

This project scrapes product details from a sample e-commerce site and saves the data into a CSV file for further analysis. The script extracts product names, prices, descriptions, and review counts using Python libraries such as `requests`, `BeautifulSoup`, `pandas`, and `lxml`.

## Features
- Scrapes product details from the URL: [Web Scraper Test Site](https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops).
- Extracted data includes:
  - Product Names
  - Prices
  - Descriptions
  - Number of Reviews
- Outputs the data to a CSV file named `products_details.csv`.

## Requirements
Install the required libraries using pip:
```
pip install requests pandas beautifulsoup4 lxml
```

## Usage
1. Run the script:
   ```
   python webscraper_p.py
   ```

2. The scraped data will be saved in `products_details.csv`.

3. To open the CSV file, use the following command in your Windows Command Line:
   ```
   start products_details.csv
   ```

## Output Example
| Product Name            | Prices | Description         | Number of Reviews |
|-------------------------|--------|---------------------|-------------------|
| HP Chromebook 14 G1    | $299   | Compact Chromebook  | 10 reviews        |
| Acer Aspire E1-510     | $249   | Affordable laptop   | 15 reviews        |







