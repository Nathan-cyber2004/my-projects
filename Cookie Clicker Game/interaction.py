from selenium import webdriver
from selenium.webdriver.common.by import By

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option('detach', True)

driver = webdriver.Edge(options = edge_options)
driver.get(url = "https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.XPATH, '/html/body/form/input[1]')
first_name.click()
first_name.send_keys('Nathaniel')

last_name = driver.find_element(By.XPATH, '/html/body/form/input[2]')
last_name.click()
last_name.send_keys('Delon')

email = driver.find_element(By.XPATH, '/html/body/form/input[3]')
email.click()
email.send_keys('natethegreat@gmail.com')

sign_up = driver.find_element(By.XPATH, '/html/body/form/button')
sign_up.click()