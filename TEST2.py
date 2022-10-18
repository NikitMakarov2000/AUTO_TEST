from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://www.saucedemo.com/"
broweser = webdriver.Chrome()
broweser.get(link)
broweser.maximize_window()

login = "standard_user"
password_all = "secret_sauce"

user_name = broweser.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login)
print("Input Login")

password = broweser.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input Password")

button_login = broweser.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("Click Login Button")

#text_products = broweser.find_element(By.XPATH, "//span[@class='title']")
#value_text_products = text_products.text
#print(value_text_products)
#assert value_text_products == "PRODUCTS"
#print("GOOD")

url = "https://www.saucedemo.com/inventory.html"
get_url = broweser.current_url
print(get_url)
assert  url == get_url
print("GOOD URL")

add_to_cart = broweser.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
add_to_cart.click()

shopping_cart = broweser.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
shopping_cart.click()

checkout = broweser.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()

first_name = broweser.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys("Jack")

last_name = broweser.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys("Backer")

postal_code = broweser.find_element(By.XPATH, "//input[@id='postal-code']")
postal_code.send_keys("1999.2000")

continue_button = broweser.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click()

finish = broweser.find_element(By.XPATH, "//button[@id='finish']")
finish.click()

broweser.close()