import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

log = ""
pas = ""
url = "https://ib.rencredit.ru/#/login"

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36")
options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="/home/Desktop/selenium/chromedriver/chromedriver")

try:
    driver.get(url=url)
    time.sleep(1)
    login_input = driver.find_element(By.ID, "username")
    login_input.send_keys(log)
    pas_input = driver.find_element(By.ID, "password")
    #pas_input.clear()
    pas_input.send_keys(pas)
    login_button = driver.find_element(By.ID, "button-button").click()
    time.sleep(3)
    driver.get("https://ib.rencredit.ru/#/cards/blocked/563594579")
    time.sleep(10)
    summ_list = (driver.find_element(By.TAG_NAME, "div").text)
    regex = r"^(\+.*) ₽"
    matches = re.finditer(regex, summ_list, re.MULTILINE)
    print([e.group(1) for e in matches])
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()