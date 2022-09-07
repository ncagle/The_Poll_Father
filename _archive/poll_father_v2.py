#_*_coding: utf-8_*_
## Poll Father v2 ##
# 2022-09-06

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class vote_bot():
    def __init__(self):
        self.driver = webdriver.Chrome(r"C:\webdrivers\chromedriver.exe")

    def vote(self):
        self.driver.get(r"https://www.dnj.com/story/sports/high-school/2022/09/04/vote-murfreesboro-area-high-school-girls-athlete-week/7906358001/")
        time.sleep(1)
        #radio = self.driver.find_element(By.ID, 'PDI_answer51184563')
        radio = self.driver.find_element_by_css_selector("input[type='radio'][value='51184563']")
        print(radio)
        radio.click()
        print(radio)
        #self.driver.close()

#while True:
bot = vote_bot()
bot.vote()



#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
#driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
# to maximize the browser window
#driver.maximize_window()
#get method to launch the URL
#driver.get(r"https://www.dnj.com/story/sports/high-school/2022/09/04/vote-murfreesboro-area-high-school-girls-athlete-week/7906358001/")
#to refresh the browser
#driver.refresh()
# identifying the radio button with xpath then click
#driver.find_element_by_xpath("//input[@value='Female']").click()
#PDI_answer51184563
#driver.find_element(By.ID, 'PDI_answer51184563')
#to close the browser
#driver.close()


#browser=webdriver.Firefox()
#browser.get("https://wiki.ubuntu.com")
#element=browser.find_element(By.ID,"searchinput")
#element.send_keys("typing")
#print(element)
#time.sleep(3)
#browser.close()
