from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# chrome Driver
service_obj = Service('/Users/Crosslynx29/Downloads/chromedriver.exe')

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detact",True)
driver = webdriver.Chrome(service=service_obj)

# driver = webdriver.Chrome(options=options)
# internal_testing = 'https://caas.trng05.ssn.ssnsgs.net:6343/caas/'


internal_testing = 'https://caas.itron-systeam02-install.eng.ssnsgs.net:6343/'
# driver.get('https://rahulshettyacademy.com')
driver.get(internal_testing)
driver.implicitly_wait(5)

print(driver.title)
print(driver.current_url)
# print(driver.)


from selenium.webdriver.common.by import By
login = driver.find_element(By.NAME,'username')
login.clear()
login.send_keys('rohasing')

password = driver.find_element(By.NAME,'password')
password.clear()
password.send_keys('Welcome@123')

driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT,'Advanced Metering Manager').click()


from selenium.webdriver import ActionChains
action = ActionChains(driver)
# wait = WebDriverWait(driver,15)
# wait.until(expected_conditions)
# action.move_to_element(driver.find_element(By.LINK_TEXT,'Devices')).perform()
# action.context_click(driver.find_element(By.LINK_TEXT,'Device Search')).perform()
# action.move_to_element(driver.find_element(By.LINK_TEXT,'Device Search')).click().perform()
# driver.find_element(By.CLASS_NAME,'formUnitLabel').send_keys('RA')
time.sleep(120)

# 'formUnitLabel'
# while True:
#     quit = input()
#     if quit =='q':
#         break
#     time.sleep()

# driver.quit()
driver.close()


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
    obistype.send_keys("0.0.0.1.0.255")

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

    driver.execute_script("window.scrollBy(0,1000)","")
        
    rst=driver.find_element(By.XPATH,'//*[@id="register_results"]/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/div/div/div/div[2]/div/div[1]').text
    print(rst)
    rst=rst.split(":")[-1]
    assert rst=='SUCCESS'
    time.sleep(1)

    dat=driver.find_element(By.XPATH,'//*[@id="register_results"]/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/div/div/div/div[2]/div/div[2]').text
    print(dat)
    dat=dat.split(":")[-1]
    assert dat=='0'
    time.sleep(1)
    print("done")
