from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


with open ("xss-payload-list.txt",'r', encoding="utf-8") as f:
    payload = f.readlines()

driver = webdriver.Firefox()


for lane in payload:
    lane=lane.strip()
    try:
        driver.get("https://demo.owasp-juice.shop/#/search?q=" + str(lane))
        time.sleep(3)
        alert = driver.switch_to.alert
        if alert is not None:
            alert.accept()
            print(f"Występuje podatność na XSS: {lane}.")
            break
    except:
        print ("Payload nie zadziałał")




