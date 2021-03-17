from selenium import webdriver

driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.myntra.com/tshirts")

sortList = driver.find_elements_by_xpath("//ul[@class='sort-list']/li/label/input")
print(len(sortList))
for value in sortList:
    print(value.get_attribute("value"))
