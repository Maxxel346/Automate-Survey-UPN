import time
import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading

def opener(name, path):
    # chromePath = os.getenv("CHROME_PATH")
    # chromePath = "E:\chromedriver-win32\chromedriver.exe"
    # D:\Acer\Music\share\buki\chromedriver_win32\chromedriver.exe
    # chromePath = "D:\Acer\Music\share\buki\chromedriver_win32\chromedriver.exe"
    # print(chromePath)
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    profile = path + "\PROFILE" + "\\" + "Profile " + name
    argument = '--user-data-dir=' + profile
    options.add_argument(argument)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    # maximize window
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # driver = webdriver.Chrome(chromePath)
    driver = webdriver.Chrome(service=service, options=options)
    return driver

driver = opener("1", os.getcwd())
driver.get("https://sadewa.upnyk.ac.id/login")
time.sleep(20)

try:    

    # # Log in
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "form_login")))
    # login_form = driver.find_element(By.ID, "form_login")
    
    # form_groups = login_form.find_elements(By.CLASS_NAME, "form-group")
    # if len(form_groups) >= 2:
    #     username_input = form_groups[0].find_element(By.TAG_NAME, "input")
    #     password_input = form_groups[1].find_element(By.TAG_NAME, "input")
        
    #     # Enter your username and password
    #     username_input.send_keys("")
    #     password_input.send_keys("")
    #     time.sleep(10)
    #     # Submit the form
    #     login_form.submit()

    # Wait for login to complete
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "form_kuisoner-p-0")))

    for i in range(10):
        # Construct the section ID
        section_id = f"form_kuisoner-p-{i}"
        print(section_id)
        # Wait for the section to be present
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, section_id)))
        
        # Find the section
        section = driver.find_element(By.ID, section_id)
        print(section)
        # Find the third element with class "pt-0" inside "p-0"
        p_0_elements = section.find_elements(By.CLASS_NAME, "p-0")
        print(len(p_0_elements))
        for p_0_element in p_0_elements:
            # if "pt-0" in p_0_element.get_attribute("class"):
            #     # click third class pt-0
            #     radio_box = p_0_element.find_elements(By.CLASS_NAME, "pt-0")[2]
            #     radio_box.click()
            try:
                radio_box = p_0_element.find_elements(By.CLASS_NAME, "pt-0")[2]
                radio_button = radio_box.find_element(By.TAG_NAME, "input")
                print("clicked" + radio_box.text)
                radio_button.click()
            except:
                print("error")


        # pt_0_elements = [element for element in p_0_elements if "pt-0" in element.get_attribute("class")]
        # print(len(pt_0_elements))
        # if len(pt_0_elements) > 2:
        #     radio_box = pt_0_elements[2]
        #     radio_box.click()
        #     print(radio_box)

        # time.sleep(500)
        # Move to the next section by clicking the second `li` inside a div with class ".actions"
        actions_div = driver.find_element(By.CSS_SELECTOR, ".actions")
        li_elements = actions_div.find_elements(By.TAG_NAME, "li")
        if len(li_elements) > 1:
            # If this is the last section, wait for a longer period before submitting
            if i == 9:
                time.sleep(5)   # Wait for a longer period before submitting
                submit_button = li_elements[2]  # The submit button is the third element
                submit_button.click()
            # Otherwise, click the next button
            else:
                next_button = li_elements[1]    # The next button is the second element
                next_button.click()
        
        # Wait for a short period to ensure the page loads the next section
        time.sleep(2)

finally:
    # Close the browser after completing the task
    # driver.quit()
    time.sleep(100)
