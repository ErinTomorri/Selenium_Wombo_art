from selenium import webdriver
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'

#space, oil on canvas Felipo Unreal Engine
#sky oasis utopia, oil on canvas Felipo Unreal Engine
#nature
#//img[@alt='Provenance']
#//img[@alt='HD']
num = 0

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
driver1 = webdriver.Chrome(PATH, options=options)
driver.get("https://app.wombo.art/")
driver1.get("https://app.wombo.art/")

text = driver.find_element_by_xpath("//input[@placeholder='Type anything']")
text.click()
text.send_keys("nature")
text = driver1.find_element_by_xpath("//input[@placeholder='Type anything']")
text.click()
text.send_keys("nature")
time.sleep(3)
prov = driver.find_element_by_xpath("//img[@alt='HD']")
prov.click()
prov = driver1.find_element_by_xpath("//img[@alt='HD']")
prov.click()
clicka = driver.find_element_by_xpath("//button[normalize-space()='Create']")
clicka.click()
clicka = driver1.find_element_by_xpath("//button[normalize-space()='Create']")
clicka.click()
time.sleep(30)


while num != 1000:
    time.sleep(10)
    save = driver.find_element_by_xpath("//button[normalize-space()='Save']")
    save.click()
    time.sleep(2)
    save = driver1.find_element_by_xpath("//button[normalize-space()='Save']")
    save.click()
    time.sleep(25)
    image = driver.find_element_by_xpath("//button[normalize-space()='Generate Again']")
    image.click()
    image = driver1.find_element_by_xpath("//button[normalize-space()='Generate Again']")
    image.click()
    time.sleep(10)
    num+=1