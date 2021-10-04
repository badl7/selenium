from selenium import webdriver

driver = webdriver.Firefox()

# Navigate to page
driver.get('http://besimgurbuz.com/software')

elements = driver.find_elements_by_css_selector('.icons')
for element in elements:
    print("**************************************")
    print(element.text)

driver.quit()