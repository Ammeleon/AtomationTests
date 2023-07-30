from selenium import webdriver
from selenium.webdriver.common.by import By
import time


'''
Предустановка:
pip install -U pytest
pip install selenium
Если при установке селениума выдает ошибку: возможно, нужно обновить pip, для этого юзаем pip install --upgrade pip
pip install selenium-webdriver
pip install webdriver-manager
По ассертам https://qaa-engineer.ru/kakie-vidy-assert-mozhno-ispolzovat-v-pytest/

'''

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
element = driver.find_element(By.XPATH, "//div[contains(text(), 'Swag Labs')]")
assert "Swag Lab" in driver.title
time.sleep(2)
login_field = driver.find_element(By.XPATH, "//input[@id='user-name']")
password_field = driver.find_element(By.XPATH, "//input[@id='password']")
login_button = driver.find_element(By.XPATH, "//input[@type='submit']")
login_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")
time.sleep(2)
login_button.click()


title_name = driver.find_element(By.XPATH, "//span[@class='title']")
assert title_name.text == "Products"
time.sleep(2)

add_to_cart_sauce_labs_backpack = driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']")
add_to_cart_sauce_labs_backpack.click()
time.sleep(2)
sauce_Labs_Bolt_T_Shirt = driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-bolt-t-shirt']")
sauce_Labs_Bolt_T_Shirt.click()
time.sleep(2)
sopping_badge = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
sopping_badge.click()
time.sleep(2)

checkout_button = driver.find_element(By.XPATH, "//button[@data-test='checkout']")
checkout_button.click()

first_name = driver.find_element(By.XPATH, "//input[@data-test='firstName']")
second_name = driver.find_element(By.XPATH, "//input[@data-test='lastName']")
zipcode = driver.find_element(By.XPATH, "//input[@data-test='postalCode']")
continue_button = driver.find_element(By.XPATH, "//input[@data-test='continue']")
time.sleep(2)
first_name.send_keys("John")
second_name.send_keys("Doe")
zipcode.send_keys("12345")
time.sleep(2)
continue_button.click()

finish_button = driver.find_element(By.XPATH, "//button[@data-test='finish']")
time.sleep(2)
finish_button.click()

driver.close()
