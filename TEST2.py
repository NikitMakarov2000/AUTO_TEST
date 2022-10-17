from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://www.saucedemo.com/"
broweser = webdriver.Chrome()
broweser.get(link)
broweser.maximize_window()

user_name = broweser.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys("standard_user")
user_name.click()

password = broweser.find_element(By.XPATH, "//input[@id='password']")
password.send_keys("secret_sauce")
password.click()

login = broweser.find_element(By.XPATH, "//input[@id='login-button']")
login.click()

add_to_cart = broweser.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
add_to_cart.click()

shopping_cart = broweser.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
shopping_cart.click()

checkout = broweser.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()

firsr_name = broweser.find_element(By.XPATH, "//input[@id='first-name']")
firsr_name.send_keys("Jack")

last_name = broweser.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys("Backer")

postal_code = broweser.find_element(By.XPATH, "//input[@id='postal-code']")
postal_code.send_keys("1999.2000")

continue_button = broweser.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click()

finish = broweser.find_element(By.XPATH, "//button[@id='finish']")
finish.click()

broweser.close()