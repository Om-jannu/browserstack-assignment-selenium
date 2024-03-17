from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from selenium.webdriver.chrome.options import Options as ChromeOptions

options = ChromeOptions()
options.set_capability('sessionName', 'BStack Assignment Selenium')

try:
    # Initialize WebDriver with options
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Load the homepage
    driver.get("https://www.flipkart.com/")

    # Search for the product
    search_box = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//input[@title="Search for Products, Brands and More" and @type="text"] | //div[@class="css-901oao css-bfa6kz r-1bo5ta7 r-13awgt0 r-1dv474o r-1enofrn"]')))
    search_box.send_keys("Samsung Galaxy S10")
    search_box.submit()
    print("Submitted the query\n")

    

    # Apply filters
    flipkart_assured_filter = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="_3879cV"]/div[@class="_3U-Vxu"]')))
    driver.execute_script("arguments[0].scrollIntoView(true);", flipkart_assured_filter)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="_3879cV"]/div[@class="_3U-Vxu"]')))
    driver.execute_script("arguments[0].click();", flipkart_assured_filter)
    print("Clicked Flipkart Assured filter\n")


    # Wait for Samsung filter to become clickable
    brand_filter = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="_3879cV" and text()="SAMSUNG"]')))
    driver.execute_script("arguments[0].scrollIntoView(true);", brand_filter)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="_3879cV" and text()="SAMSUNG"]')))
    driver.execute_script("arguments[0].click();", brand_filter)
    print("Clicked Samsung filter\n") 

    # Sort by Price - High to Low
    sort_price_high_to_low = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="_10UF8M" and text()="Price -- High to Low"]')))
    sort_price_high_to_low.click()
    print("Clicked Flipkart high to low sorting\n")

    # Wait for the results to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='_1AtVbE']")))
    print("Waiting to load results\n")

    # Extract and print the results
    product_names = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@class="_4rR01T"]')))
    display_prices = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@class="_30jeq3 _1_WHN1"]')))
    product_links = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//a[@class="_1fQZEK"]')))

    for name, price, link in zip(product_names, display_prices, product_links):
        print("Product Name:", name.text)
        print("Display Price:", price.text)
        print("Link to Product Details Page:", link.get_attribute('href'))
        print("\n")
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Product details displayed on the consle"}}')   
except Exception as e:
    print("An error occurred:", e)
    message = 'Exception: ' + str(e)
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')
finally:
    # Close the WebDriver
    driver.quit()
