from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#this will help the site wait while loading
from selenium.webdriver.support.ui import WebDriverWait
#get access to the keys on the website
from selenium.webdriver.common.keys import Keys
import time


#path to chrome driver
service = Service(executable_path=r"C:\Users\HP\Desktop\Setups\chrome-win64")


#select the browser to use
driver = webdriver.Chrome()

#open a website
#driver.get("https://finance.yahoo.com")

#access elements on the webpage (in this case we are accessing the search bar) and wait until the serch bar is visible
#search = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "ybar-sbq")))

#the text you wanna search for, it basically helps to send the text to the serch box in the page
#search.send_keys("APPL")

#this helps to press the search button on the website
#search.send_keys(Keys.RETURN)

#print the resulit of the search
#print(search.text)

#print out the page source
#print(driver.page_source)

#set the time to delay the program by 100 seconds
#time.sleep(100)

#get the website
driver.get("https://tech-with-tim-merch-shop.creator-spring.com/")

#using try and except to avoid error incase the element does not load on time

"""search = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.TAG_NAME, "input")))
search.send_keys("hoodie")
search.send_keys(Keys.RETURN)
"""
try:
    container = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CLASS_NAME, "Products_mainContainer__F9kPt")))
    print(container.text)
except:
    driver.quit()

#print(search.text)
time.sleep(100)




#end the driver session
#titles = course.text
#links = course.get_attribute("href")"""
 #print(course.text)
driver.quit()