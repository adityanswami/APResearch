# import random

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# import pandas



driver = webdriver.Chrome()
driver.get("https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/analysis/game/live/123456?tab%3Dreview")
username = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(driver.find_element(By.NAME, "_username")))
username.send_keys("----username here----")
password = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(driver.find_element(By.NAME, "_password")))
password.send_keys("----password here----")
submit_button = driver.find_element(By.NAME, "login")
submit_button.click()
driver.implicitly_wait(10)
html = driver.page_source

# beginning = 0
# end = 177777
# gameID = random.randint(beginning, end)


soup = BeautifulSoup(html, "html.parser")


white_rating = str(soup.findAll("span", class_="user-tagline-rating user-tagline-white")[1])[59:63]
black_rating = str(soup.findAll("span", class_="user-tagline-rating user-tagline-white")[0])[59:63]
print(white_rating)
print(black_rating)