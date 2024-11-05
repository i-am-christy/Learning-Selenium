#libraries to scrape a website protected by cloudflare
from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#create a new instance of Chrome
chrome = Chrome()

#navigate the website
chrome.get("https://www.leolist.cc/")

time.sleep(100)
#close the browser
chrome.close()