import time

from selenium import webdriver

chromeOptions =webdriver.ChromeOptions()
# chromeOptions.set_capability("platformName", "")
chromeOptions.set_capability("browserName","chrome")

driver=webdriver.Remote(
   command_executor="http://localhost:4444/wd/hub",
       options=chromeOptions
)
for i in range(7):
    driver.get("https://www.selenium.dev/downloads/")
    # time.sleep(5)

