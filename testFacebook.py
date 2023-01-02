from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
email = ""
password = ""

driver.get("http://www.facebook.com")
elem = driver.find_element(By.ID,"email")
elem.send_keys(email)
elem = driver.find_element(By.ID,"pass")
elem.send_keys(password)
elem.send_keys(Keys.RETURN)
driver.get("https://facebook.com/messages/"+"w")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()
# elem = driver.find_element_by_css_selector("div textarea.uiTextareaNoResize")
# elem.send_keys("python test")
# elem.send_keys(Keys.RETURN)