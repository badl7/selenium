from selenium import webdriver

driver = webdriver.Firefox()

# Navigate to page
driver.get('http://besimgurbuz.com')
print(driver.title)

driver.quit()