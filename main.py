from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains

try:
    # Initialize WebDriver (assuming Chrome WebDriver)
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Load the homepage
    driver.get("https://www.flipkart.com/")

    # Search for the product
    search_box = driver.find_element(By.XPATH, '//input[@title="Search for Products, Brands and More"]')
    search_box.send_keys("Samsung Galaxy S10")
    search_box.submit()
    print("Submitted the query\n")

    # Click on "Mobiles" category
    mobiles_category = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="_1jJQdf _2Mji8F"]')))
    mobiles_category.click()
    print("Clicked Mobiles\n")

    # Apply filters
    flipkart_assured_filter = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="_3U-Vxu"]')))
    flipkart_assured_filter.click()
    print("Clicked Flipkart Assured filter\n")

    # Scroll to Samsung filter
    driver.execute_script("arguments[0].scrollIntoView(true);", flipkart_assured_filter)

    # Move to Samsung filter
    action = ActionChains(driver)
    action.move_to_element(flipkart_assured_filter).perform()

    # Wait for Samsung filter to become clickable
    brand_filter = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="_3879cV" and text()="SAMSUNG"]')))
    brand_filter.click()
    print("Clicked Samsung filter\n")

    # Sort by Price - High to Low
    sort_price_high_to_low = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="_10UF8M" and text()="Price -- High to Low"]')))
    sort_price_high_to_low.click()
    print("Clicked Flipkart high to low sorting\n")

    # Wait for the results to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='_1AtVbE']")))
    print("Waiting to load results\n")

    # Read the results
    product_names = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@class="_4rR01T"]')))
    display_prices = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@class="_30jeq3 _1_WHN1"]')))
    product_links = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//a[@class="_1fQZEK"]')))

    # Create and print the list of parameters
    # Print the list of parameters directly without creating a results list
    for name, price, link in zip(product_names, display_prices, product_links):
        print("Product Name:", name.text)
        print("Display Price:", price.text)
        print("Link to Product Details Page:", link.get_attribute('href'))
        print("\n")

except (TimeoutException, NoSuchElementException, ElementClickInterceptedException) as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the WebDriver
    driver.quit()
