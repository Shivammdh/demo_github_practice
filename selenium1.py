import time
from selenium import webdriver
from selenium.webdriver.common.by import By

drive=webdriver.Chrome()
drive.maximize_window()
drive.get("https://rahulshettyacademy.com/AutomationPractice/")
all_links=drive.find_elements(By.XPATH,"//div[@class=' footer_top_agile_w3ls gffoot footer_style']/table//tr/td[2]/ul/li//a")
for link in all_links:
    print(link.text)
# drive.find_element(By.CSS_SELECTOR,"#exampleInputPassword1").send_keys("Chandu@123")
# email=drive.find_element(By.NAME,"email")
# email.send_keys("chandu@gmail.com")
# print(email.get_attribute('value'))
# print(email.get_attribute('name'))

time.sleep(5)
drive.close()


