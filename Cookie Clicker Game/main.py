from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initializing Webdriver
service = Service(executable_path = "msedgedriver.exe")
driver = webdriver.Edge(service = service)

# Required IDs
language_id = "langSelect-EN"
cookie_id = "bigCookie"
cookies_id = "cookies"

product_price_prefix = "productPrice"
product_prefix = "product"

URL = "https://orteil.dashnet.org/cookieclicker/"
driver.get(URL)


WebDriverWait(driver, 5).until (
  EC.presence_of_element_located((By.ID, language_id))
)

select_language = driver.find_element(By.ID, language_id)
select_language.click()

WebDriverWait(driver, 5).until(
  EC.presence_of_element_located((By.ID, cookie_id))
)
click_cookie = driver.find_element(By.ID, cookie_id)

while True:
  click_cookie.click()
  cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
  cookies_count = int(cookies_count)

  for i in range(4):
    product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

    if not product_price.isdigit():
      continue

    product_price = int(product_price)

    if cookies_count >= product_price:
      product = driver.find_element(By.ID, product_prefix + str(i))
      product.click()
      break