from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/ankush.singal/Desktop/Development/chromedriver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com/dp/B09F6XHB4C/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0")
price = driver.find_element(By.CLASS_NAME,"a-offscreen")
print(price.get_attribute('innerHTML'))
driver.quit()