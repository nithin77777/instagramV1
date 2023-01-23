import selenium

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
import warnings
import macmouse
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
import requests
from time import sleep
import logging
import xlsxwriter
import selenium.webdriver.chrome.service

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--headless")
service = webdriver.chrome.service.Service(executable_path="/Users/nithinsaikrishna/Downloads/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

# --> LOGIN
# def login_now():
driver.get("https://www.instagram.com/accounts/login")
time.sleep(3)
username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
username.clear()
password.clear()
username.send_keys("capnxtglobal9798@gmail.com")
password.send_keys('padma1974#P')        #("padma1974#P")
login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "_acan._acap._acas._aj1-"))).click()
time.sleep(7)

# --> SAVE LOGIN INFO?
notnow1=WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not now")]'))).click()

# --> TURN OFF NOTIFICATIONS
time.sleep(7)
notnow2=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()



time.sleep(5)

post = driver.get("https://www.instagram.com/p/CnOrYg5y2Uh/")
insights = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "_acan._acao._acas._aj1-"))).click()

time.sleep(3)


# caption = driver.find_element(By.CLASS_NAME, "_aacl._aaco._aacu._aacx._aad7._aade").text
# print(caption)


# def insights():
# likesFrontPage = driver.find_element(By.CLASS_NAME, "_aacl._aaco._aacw._aacx._aada._aade").text

elements=driver.find_elements(By.TAG_NAME,"span")
# print(elements)
# element = elements.find_element(By.CLASS_NAME,"x9f619.x78zum5.x1c4vz4f.xs83m0k.xdl72j9.x1q0g3np.x1a2a7pz.x67bb7w.x1n2onr6.x2lwn1j.xeuugli")

#Loop Start_________________________________________
insights_list = list()
count=0
for el in elements:
    # print(el.text)
    insights_list.append(el.text)
    count+=1
print(count)
#loop End____________________________________________
print("Element One: " + insights_list[0])
print("Element two: " + insights_list[1])
print("Element three: " + insights_list[2])
print("Element Four: " + insights_list[3])
print("Element Five: " + insights_list[4])
print("Element Six: " + insights_list[5])
print("Element Seven: " + insights_list[6])
print("Element Eight: " + insights_list[7])
print("Element Nine: " + insights_list[8])
print("Element : " + insights_list[9])
print("Element : " + insights_list[10])
print("Element : " + insights_list[11])
print("Element : " + insights_list[12])
print("Element : " + insights_list[13])
print("Element : " + insights_list[14])
print("Element : " + insights_list[15])
print("Element : " + insights_list[16])
print("Element : " + insights_list[17])
print("Element : " + insights_list[18])
print("Element : " + insights_list[19])
print("Element : " + insights_list[20])
print("Element : " + insights_list[21])
print("Element : " + insights_list[22])
print("Element : " + insights_list[23])
print("Element : " + insights_list[24])
print("Element : " + insights_list[25])
print("Element : " + insights_list[26])
print("Element : " + insights_list[27])
print("Element : " + insights_list[28])
print("Element : " + insights_list[29])
print("Element : " + insights_list[30])
print("Element : " + insights_list[31])
print("Element : " + insights_list[32])
print("Element : " + insights_list[33])
print("Element : " + insights_list[34])
print("Element : " + insights_list[35])
print("Element : " + insights_list[36])
print("Element : " + insights_list[37])
print("Element : " + insights_list[38])
print("Element : " + insights_list[39])
print("Element : " + insights_list[40])
print("Element : "+ insights_list[41])
print("Element : " + insights_list[42])
print("Element : " + insights_list[43])
print("Element : " + insights_list[44])






# elementNew = driver.find_element(By.CLASS_NAME,"x9f619.x78zum5.x1c4vz4f.xs83m0k.xdl72j9.x1q0g3np.x1a2a7pz.x67bb7w.x1n2onr6.x2lwn1j.xeuugli")
# print(elementNew.get_attribute("innerHTML"))
# except:
#     print('error at retrieving SPANS!!!')











# Getting Likes From XPATH and SPAN element
# likesAd = driver.find_element(By.XPATH, "//div[@class='x9f619 x78zum5 x1c4vz4f xs83m0k xdl72j9 x1q0g3np x1a2a7pz x67bb7w x1n2onr6 x2lwn1j xeuugli']/span").text
# except:
#     print("Stopped At Likes Block!! LINE 80")


# Getting Comments From XPath and Comments Element


# commentsAd = driver.find_element(By.XPATH, "//div[@class='x9f619.x78zum5.x1c4vz4f.xs83m0k.xdl72j9.x1q0g3np.x1a2a7pz.x67bb7w.x1n2onr6.x2lwn1j.xeuugli']/span").text

# Getting Reach From XPATH and SPAN
# locate elements by class name
# elements = driver.find_element(By.CLASS_NAME,'x9f619.x78zum5.x1c4vz4f.xs83m0k.xdl72j9.x1q0g3np.x1a2a7pz.x67bb7w.x1n2onr6.x2lwn1j.xeuugli')

# iterate over the elements and retrieve the text or attribute value
# for element in elements:
#     text = element.text
#     attribute_value = element.get_attribute("span")
#     print(text, attribute_value)






# commentAD =



