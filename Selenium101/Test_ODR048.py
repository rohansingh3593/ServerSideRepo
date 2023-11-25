"""
step1-Open AMM

step2-click on device Search by entering name

step3-click on a particular device

step4-click on a On demand read option

step5-from Read type : Select the "Arbitrary meter read" from drop down list

step6-Request type: Select the "Read" option 

step7-Class ID:1

step8-Obis code: 1.0.0.2.0.255

step9-Attribute: 2

step10-Push result to JMS: select "No" option

step11-click on read and wait for the response

step12-check the read result success response 

"""

import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_case():
        
    driver=webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://caas.itron-systeam02-install.eng.ssnsgs.net:6343/caas/")
    driver.maximize_window()
    title = driver.title
    name = driver.find_element(By.NAME, "username").send_keys("aman.srivastava")
    password=driver.find_element(By.ID,"password").send_keys("Welcome@123")
    button=driver.find_element(By.ID ,"btn_submit")
    button.click()

    "step-1"
    opton1=driver.find_element(By.LINK_TEXT,'Advanced Metering Manager')
    opton1.click()
    devic=driver.find_element(By.ID,"devices_tab")
    devic.click()
    time.sleep(1)

    "step-2"
    name1= driver.find_element(By.ID, "device_name").send_keys("CL_W1PH_1_Cellular_8497")
    time.sleep(1)

    searchdev=driver.find_element(By.CSS_SELECTOR,"#DeviceSearch > div.tac.ptm > button")
    searchdev.click()
    time.sleep(1)

    "step-3"
    opton12=driver.find_element(By.LINK_TEXT,'CL_W1PH_1_Cellular_8497')
    opton12.click()

    "step-4"
    read1=driver.find_elements(By.XPATH,'//*[@id="read"]/a')
    read1[0].click()


    "step-5"
    drp=driver.find_element(By.ID,"odr_read_type")
    drp.click()
    text='Arbitary Meter Read'
    drp.send_keys(text)
    drp.click()
    time.sleep(1)

    "step-6"
    reqtype=driver.find_element(By.ID,"dlmsRequestType").send_keys(text)
    # text='Read'
    # reqtype.send_keys(text).click()
    time.sleep(1)
    "step-7"
    ctype=driver.find_element(By.ID,"arbitrarydlmscommandjob_classId")
    ctype.clear()
    ctype.send_keys('1')

    "step-8"
    obistype=driver.find_element(By.ID,"arbitrarydlmscommandjob_obisCode")
    obistype.clear()
    obistype.send_keys("1.0.0.2.0.255")

    "step-9"
    attype=driver.find_element(By.XPATH,'//*[@id="arbitrarydlmscommandjob_attributeId"]')
    attype.clear()
    attype.send_keys("2")


    "step-10"
    drp2=driver.find_element(By.ID,"push_to_jms")
    drp2.click()
    drp2.send_keys('no')
    drp2.click()

    "step-11"
    button=driver.find_element(By.ID ,"read_button")
    button.click()

    wait = WebDriverWait(driver,90)
    wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="hidden_results"]/h2')))

    expnd=driver.find_element(By.CSS_SELECTOR,"#register_results > tbody > tr:nth-child(2) > td:nth-child(2) > table > tbody > tr > td:nth-child(2) > button")
    expnd.click()

    table=driver.find_elements(By.ID,'odr_results_div')

    for data in table:
        print(data.text)

    time.sleep(2)

    print("#################################################")
    
    rst=driver.find_element(By.XPATH,'//*[@id="register_results"]/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/div/div/div/div[2]/div/div[1]').text
    print(rst)
    rst=rst.split(":")[-1]
    assert rst=='SUCCESS'
    time.sleep(1)

    dat=driver.find_element(By.XPATH,'//*[@id="register_results"]/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/div/div/div/div[2]/div/div[2]').text
    print(dat)
    dat=dat.split(":")[-1]
    assert dat=='97 77 49 48 48 45 76 45 65 55 48 50 48 50 49 50'
    time.sleep(1)
    print("done")
