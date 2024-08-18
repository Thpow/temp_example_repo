import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from ui import select_random_from_dropdown
import time

chrome_options = Options()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.roblox.com")

for i in range(3):
    select_random_from_dropdown("/html/body/div[3]/div/section/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div["+str(i+1)+"]/select", driver)

time.sleep(10)

driver.quit()