# import random
import random

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from threading import Timer
import time
import pandas


def checkIsStandard(gameID):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/game/live/"+str(gameID))
    username = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(driver.find_element(By.NAME, "_username")))
    username.send_keys("---username---")
    password = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(driver.find_element(By.NAME, "_password")))
    password.send_keys("---password---")
    submit_button = driver.find_element(By.NAME, "login")
    submit_button.click()
    #t = Timer(15, wai1(driver))
    #t.start()
    time.sleep(2)
    info_button = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[1]/button[2]")
    info_button.click()
    time.sleep(0.5)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    cl = str(soup.find(class_="archive-game-info-component"))
    if "Variant: Standard (Rated)" in cl:
        time_control = cl[cl.find("Time")+6:cl.find("Variant") - 12]
        if "min" in time_control:
            base = int(time_control[:-4])
            increment = 0
            if base < 3:
                return(True, "Bullet")
            elif base < 10:
                return(True, "Blitz")
            else:
                return (True, "Rapid")
        else:
            base = int(time_control[:time_control.find("|")-1])
            increment = int(time_control[time_control.find("|")+2:])

            if (base + (40/60)*increment) < 3:
                return (True, "Bullet")
            elif (base + (40/60)*increment) < 10:
                return (True, "Blitz")
            else:
                return (True, "Rapid")
    return False

#options = webdriver.ChromeOptions()
#options.add_experimental_option("detach", True)
def getInfo(gameID):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/analysis/game/live/"+str(gameID)+"?tab%3Dreview")
    username = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(driver.find_element(By.NAME, "_username")))
    username.send_keys("---username---")
    password = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(driver.find_element(By.NAME, "_password")))
    password.send_keys("---password---")
    submit_button = driver.find_element(By.NAME, "login")
    submit_button.click()
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    white_rating = str(soup.findAll("span", class_="user-tagline-rating user-tagline-white")[1])[59:-11]
    black_rating = str(soup.findAll("span", class_="user-tagline-rating user-tagline-white")[0])[59:-11]
    white_CAPS = str(soup.findAll(class_="accuracy-score-value")[0])[34:-6]
    black_CAPS = str(soup.findAll(class_="accuracy-score-value")[1])[34:-6]
    return(white_rating, black_rating, white_CAPS, black_CAPS)

df = pandas.DataFrame(columns= ["Game ID", "Time Category", "Rating", "CAPS"])
n = 18
for i in range(250):
    gameID = random.randint(69124249559-1, 100485096043)
    try:
        (checked, category) = checkIsStandard(gameID)
        (white_rating, black_rating, white_CAPS, black_CAPS) = getInfo(gameID)
        df.loc[len(df.index)] = [gameID, category, white_rating, white_CAPS]
        df.loc[len(df.index)] = [gameID, category, black_rating, black_CAPS]
        print(gameID, category, black_rating, black_CAPS)
    except:
        pass
    print(i, n)
df.to_excel("Data"+str(n)+".xlsx")
n += 1
for i in range(250):
    gameID = random.randint(69124249559-1, 100485096043)
    try:
        (checked, category) = checkIsStandard(gameID)
        (white_rating, black_rating, white_CAPS, black_CAPS) = getInfo(gameID)
        df.loc[len(df.index)] = [gameID, category, white_rating, white_CAPS]
        df.loc[len(df.index)] = [gameID, category, black_rating, black_CAPS]
        print(gameID, category, black_rating, black_CAPS)
    except:
        pass
    print(i, n)
df.to_excel("Data"+str(n)+".xlsx")
n+=1
for i in range(250):
    gameID = random.randint(69124249559-1, 100485096043)
    try:
        (checked, category) = checkIsStandard(gameID)
        (white_rating, black_rating, white_CAPS, black_CAPS) = getInfo(gameID)
        df.loc[len(df.index)] = [gameID, category, white_rating, white_CAPS]
        df.loc[len(df.index)] = [gameID, category, black_rating, black_CAPS]
        print(gameID, category, black_rating, black_CAPS)
    except:
        pass
    print(i, n)
df.to_excel("Data"+str(n)+".xlsx")
n+=1
for i in range(250):
    gameID = random.randint(69124249559-1, 100485096043)
    try:
        (checked, category) = checkIsStandard(gameID)
        (white_rating, black_rating, white_CAPS, black_CAPS) = getInfo(gameID)
        df.loc[len(df.index)] = [gameID, category, white_rating, white_CAPS]
        df.loc[len(df.index)] = [gameID, category, black_rating, black_CAPS]
        print(gameID, category, black_rating, black_CAPS)
    except:
        pass
    print(i, n)
df.to_excel("Data"+str(n)+".xlsx")
n+=1
for i in range(250):
    gameID = random.randint(69124249559-1, 100485096043)
    try:
        (checked, category) = checkIsStandard(gameID)
        (white_rating, black_rating, white_CAPS, black_CAPS) = getInfo(gameID)
        df.loc[len(df.index)] = [gameID, category, white_rating, white_CAPS]
        df.loc[len(df.index)] = [gameID, category, black_rating, black_CAPS]
        print(gameID, category, black_rating, black_CAPS)
    except:
        pass
    print(i, n)
df.to_excel("Data"+str(n)+".xlsx")
n+=1
for i in range(250):
    gameID = random.randint(69124249559-1, 100485096043)
    try:
        (checked, category) = checkIsStandard(gameID)
        (white_rating, black_rating, white_CAPS, black_CAPS) = getInfo(gameID)
        df.loc[len(df.index)] = [gameID, category, white_rating, white_CAPS]
        df.loc[len(df.index)] = [gameID, category, black_rating, black_CAPS]
        print(gameID, category, black_rating, black_CAPS)
    except:
        pass
    print(i, n)
df.to_excel("Data"+str(n)+".xlsx")
n+=1
for i in range(250):
    gameID = random.randint(69124249559-1, 100485096043)
    try:
        (checked, category) = checkIsStandard(gameID)
        (white_rating, black_rating, white_CAPS, black_CAPS) = getInfo(gameID)
        df.loc[len(df.index)] = [gameID, category, white_rating, white_CAPS]
        df.loc[len(df.index)] = [gameID, category, black_rating, black_CAPS]
        print(gameID, category, black_rating, black_CAPS)
    except:
        pass
    print(i, n)
df.to_excel("Data"+str(n)+".xlsx")
n+=1
for i in range(250):
    gameID = random.randint(69124249559-1, 100485096043)
    try:
        (checked, category) = checkIsStandard(gameID)
        (white_rating, black_rating, white_CAPS, black_CAPS) = getInfo(gameID)
        df.loc[len(df.index)] = [gameID, category, white_rating, white_CAPS]
        df.loc[len(df.index)] = [gameID, category, black_rating, black_CAPS]
        print(gameID, category, black_rating, black_CAPS)
    except:
        pass
    print(i, n)
df.to_excel("Data"+str(n)+".xlsx")
n+=1