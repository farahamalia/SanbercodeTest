# SanbercodeTest
# Tugas Day 17
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_01login_positive(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com") # buka situs
        browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.ID, "user-name").send_keys("standard_user") # isi username
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.ID, "login-button").click() # klik tombol sign in
        time.sleep(1) 
    
    def test_02login_negative_wrong_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com") # buka situs
        browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.ID, "user-name").send_keys("standard_user") # isi username
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys("salah") # isi password
        time.sleep(1)
        browser.find_element(By.ID, "login-button").click() # klik tombol sign in
        time.sleep(1)
        
        response_message = browser.find_element(By.CLASS_NAME,"error-message-container").text
        self.assertEqual(response_message, 'Epic sadface: Username and password do not match any user in this service')    
   
    def test_03login_negative_empty_email_and_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com") # buka situs
        browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.ID, "user-name").send_keys("") # isi username
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID, "login-button").click() # klik tombol sign in
        time.sleep(1)
        
        response_message = browser.find_element(By.CLASS_NAME,"error-message-container").text
        self.assertEqual(response_message, 'Epic sadface: Username is required')
    
    def test_04add_and_remove_product(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com") # buka situs
        browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.ID, "user-name").send_keys("standard_user") # isi username
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.ID, "login-button").click() # klik tombol sign in
        time.sleep(1)       
        browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click() # pilih product
        time.sleep(1) 
        browser.find_element(By.ID, "remove-sauce-labs-backpack").click() # remove product
        time.sleep(1) 
    
    def test_05checkOut_negative_empty_field(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com") # buka situs
        browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.ID, "user-name").send_keys("standard_user") # isi username
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.ID, "login-button").click() # klik tombol sign in
        time.sleep(1)       
        browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click() # pilih product
        time.sleep(1) 
        browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()  
        time.sleep(1)
        browser.find_element(By.ID, "checkout").click() #setuju melakukan pembelian
        time.sleep(1)
        browser.find_element(By.ID, "first-name").send_keys("") # isi firstname
        time.sleep(1)
        browser.find_element(By.ID, "last-name").send_keys("") # isi lastname
        time.sleep(1)
        browser.find_element(By.ID, "postal-code").send_keys("") # isi postal code
        time.sleep(1)
        browser.find_element(By.ID, "continue").click() # klik tombol continue
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.CLASS_NAME,"error-message-container").text
        self.assertEqual(response_message, 'Error: First Name is required')   
      
    def test_06checkOut_positive(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com") # buka situs
        browser.maximize_window()
        time.sleep(3)
        browser.find_element(By.ID, "user-name").send_keys("standard_user") # isi username
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.ID, "login-button").click() # klik tombol sign in
        time.sleep(1)       
        browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click() # pilih product
        time.sleep(1) 
        browser.find_element(By.CLASS_NAME, "shopping_cart_link").click() 
        time.sleep(1)
        browser.find_element(By.ID, "checkout").click() #setuju melakukan pembelian
        time.sleep(1)
        browser.find_element(By.ID, "first-name").send_keys("test") # isi firstname
        time.sleep(1)
        browser.find_element(By.ID, "last-name").send_keys("test2") # isi lastname
        time.sleep(1)
        browser.find_element(By.ID, "postal-code").send_keys("12345") # isi postal code
        time.sleep(1)
        browser.find_element(By.ID, "continue").click() # klik tombol continue
        time.sleep(1)
        browser.find_element(By.ID, "finish").click() # klik tombol finish
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.CLASS_NAME,"complete-text").text
        
        self.assertEqual(response_message, 'Your order has been dispatched, and will arrive just as fast as the pony can get there!')     
  
    
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
