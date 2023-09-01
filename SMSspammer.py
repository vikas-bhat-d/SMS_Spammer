##created by Vikas Bhat D
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


import os
import random
import wget
import time

"""options=Options()
options.add_experimental_option("detach", True)

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)"""

no=input("Enter number: ")
def meesho(no):
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.meesho.com/auth?redirect=https%3A%2F%2Fwww.meesho.com%2F&source=profile&entry=header&screen=HP")

    phone_no=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[type='tel']")))

    phone_no.send_keys(no)

    login=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']")))
    login.click()
    time.sleep(2)

def rummycircle(no):
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.rummycircle.com/?pid=gadwords_af&af_pmod_priority=equal&af_pmod_lookback_window=7d&is_retargeting=true&utm_source=gadwords&utm_medium=Search&utm_content=ade1467&utm_term=e_rummy%20circle&utm_campaign=SE-Top_10_Brand_2_DT_KA&utm_placement=rummy_circle_EM&gclid=EAIaIQobChMI77O7h_yIgQMVi199Ch0XtQscEAAYASAAEgJZl_D_BwE")

    phone_no=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[type='tel']")))

    phone_no.send_keys(no)

    login=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[id='getStarted']")))
    login.click()
    time.sleep(2)

def urbanic(no):
    #driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    options=Options()
    options.add_experimental_option("detach", False)

    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    driver.get("https://in.urbanic.com/register?callback=https://in.urbanic.com/?widgetid=13&detail_type=others&utm_medium=ppc&biz_type=ppc&channel=google&pid=dHmLNsxX168&other_detail_id=search&gclid=EAIaIQobChMIvJfH9-6IgQMV0dHCBB0Rtg-lEAAYASAAEgIUKPD_BwE&ad_id=649933982559&short_link_uid=D849F0CF506049778FFBAC9C5732E557&adset_id=146953018495&keyword=urbanic&campaign_id=19749490692&utm_source=google&short_key=ny3mnz&utm_content=others")

    phone_no=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[id='userName']")))

    phone_no.send_keys(no)

    login=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[class='ant-btn ant-btn-default']")))
    login.click()
    time.sleep(2)
    driver.close()

    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://in.urbanic.com/login?ad_id=649933982559&adset_id=146953018495&biz_type=ppc&callback=https://in.urbanic.com/?widgetid=13&campaign_id=19749490692&channel=google&detail_type=others&keyword=urbanic&other_detail_id=search&pid=dHmLNsxX168&short_key=ny3mnz&short_link_uid=D849F0CF506049778FFBAC9C5732E557")

    phone_no=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[id='userName']")))

    phone_no.send_keys(no)

    login=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[class='ant-btn ant-btn-default']")))
    login.click()
    time.sleep(2)
    driver.close()

def ullu(no):
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://ullu.app/#/login")
    phone_no=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[type='tel']")))

    phone_no.send_keys(no)
    time.sleep(2)
    login=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='button']")))
    login.click()
    time.sleep(5)
    driver.close()


for i in range(15):
    res=random.choice([1,2,3,4])
    if(res==1):
        meesho(no)
    elif(res==2):
        rummycircle(no)
    elif(res==3):
        urbanic(no)
    elif(res==4):
        ullu(no)

