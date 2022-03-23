from matplotlib import collections
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import glob
import pyautogui
import os
import sys


path = "enter path to ur images"
des="enter ur description here"
num = 0
num1 = 64
# chrome
PATH = 'C:\Program Files (x86)\chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")
options.add_experimental_option(
    "excludeSwitches", ["enable-automation", "enable-logging"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option(
    'prefs', {'intl.accept_languages': 'en_US,en'})
options.add_argument("--mute-audio")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-features=UserAgentClientHint')
options.add_argument("download.default_directory=C:/Users/Erin Tomorri/Desktop/nft/final nft")
    
driver = webdriver.Chrome(PATH, options=options)

a= os.listdir(path)

driver.get('https://opensea.io/login?referrer=%2Faccount')

user = input('y/n')
while user != 'y':
    user = input('y/n')

for num in range(len(a)):
    time.sleep(8)
    time.sleep(2)
    create = driver.find_element_by_xpath("//a[normalize-space()='Create']")
    create.click()
    time.sleep(2)
    img = driver.find_element_by_xpath("//div[@aria-label='Select an image, video, audio or 3D model file']")
    img.click()
    time.sleep(15)
    pyautogui.write(a[num]) 
    pyautogui.press('enter')
    time.sleep(2)
    name = driver.find_element_by_xpath("//input[@id='name']")
    name.click()
    name.send_keys("Zima-Blue#"+str(num1))
    time.sleep(2)
    des = driver.find_element_by_xpath("//textarea[@id='description']")
    des.click()
    des.send_keys(des)
    time.sleep(2)
    collection = driver.find_element_by_xpath("//input[@id='collection']")
    collection.click()
    chain = driver.find_element_by_xpath("//input[@id='chain']")
    chain.click()
    chain.send_keys(Keys.TAB)
    time.sleep(4)
    chain = driver.find_element_by_xpath("//*[contains(text(), 'Polygon')]")
    chain.click()
    time.sleep(2)
    create1 = driver.find_element_by_xpath("//button[normalize-space()='Create']")
    create1.click()
    time.sleep(3)
    time.sleep(30)
    try:
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div/div/div[2]/button/i')))
    finally:
        num += 1
        num1 += 1

