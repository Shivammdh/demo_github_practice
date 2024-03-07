import time
from selenium import webdriver
from selenium.webdriver.common.by import By

drive=webdriver.Chrome()
drive.maximize_window()
drive.get("https://rahulshettyacademy.com/AutomationPractice/")
all_links=drive.find_elements(By.XPATH,"//div[@class=' footer_top_agile_w3ls gffoot footer_style']/table//tr/td[2]/ul/li//a")
for link in all_links:
    print(link.text)

all_radio=drive.find_elements(By.XPATH,"//div[@id='radio-btn-example']/fieldset/label/input")
for radio in all_radio:
    print(radio.is_displayed())
    radio.click()
    print(radio.is_selected())

all_checkbox=drive.find_elements(By.XPATH,"//div[@id='checkbox-example']/fieldset/label/input")
for checkbox in all_checkbox:
    print(checkbox.is_displayed())
    checkbox.click()
    print(checkbox.is_selected())


time.sleep(5)
drive.close()


