# import random

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from threading import Timer

# import pandas
def wai():
    global white_rating, black_rating, white_CAPS, black_CAPS
    html = driver.page_source

    # beginning = 0
    # end = 177777
    # gameID = random.randint(beginning, end)

    soup = BeautifulSoup(html, "html.parser")

    white_rating = str(soup.findAll("span", class_="user-tagline-rating user-tagline-white")[1])[59:-11]
    black_rating = str(soup.findAll("span", class_="user-tagline-rating user-tagline-white")[0])[59:-11]
    white_CAPS = str(soup.findAll(class_="accuracy-score-value")[0])[34:-6]
    black_CAPS = str(soup.findAll(class_="accuracy-score-value")[1])[34:-6]
    print(white_rating)
    print(black_rating)
    print(white_CAPS)
    print(black_CAPS)


driver = webdriver.Chrome()
driver.get("https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/analysis/game/live/123456?tab%3Dreview")
username = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(driver.find_element(By.NAME, "_username")))
username.send_keys("---username here---")
password = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(driver.find_element(By.NAME, "_password")))
password.send_keys("---password---")
submit_button = driver.find_element(By.NAME, "login")
submit_button.click()
t = Timer(5, wai)
t.start()

