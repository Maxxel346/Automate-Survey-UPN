import time
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





USERNAME = "fill in your username here"
PASSWORD = "fill in your password here"









def opener(name, path):
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

def makeSureNameAndPassword():
    # Check if the username and password are filled in
    if USERNAME == "fill in your username here":
        print("Please fill in your username in the USERNAME variable")
    if PASSWORD == "fill in your password here":
        print("Please fill in your password in the PASSWORD variable")
    if USERNAME == "fill in your username here" or PASSWORD == "fill in your password here":
        print("Please fill in your username and password in the USERNAME and PASSWORD variable")
    
    # Automatically exit the program if the username and password are not filled in
    if USERNAME != "fill in your username here" and PASSWORD != "fill in your password here":
        pass
    else:
        sys.exit()

driver = opener("1", os.getcwd())
driver.get("https://sadewa.upnyk.ac.id/login")
time.sleep(20)


try:    
    # Attempt to login
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "form_login")))

    # Find the login form
    login_form = driver.find_element(By.ID, "form_login")

    # Fill in the login form
    if login_form is not None:
        form_groups = login_form.find_elements(By.CLASS_NAME, "form-group")
        if len(form_groups) >= 2:
            username_input = form_groups[0].find_element(By.TAG_NAME, "input")
            password_input = form_groups[1].find_element(By.TAG_NAME, "input")

            # Check if the username and password are filled in
            makeSureNameAndPassword()

            # Enter your username and password
            username_input.send_keys(USERNAME)
            password_input.send_keys(PASSWORD)

            # Wait for a short period to ensure the page loads the captcha and manually solve it
            # +----------------------------------------+
            # |  Feel free to adjust the waiting time  |
            # +----------------------------------------+
            time.sleep(20)

            # Submit the form
            login_form.submit()

    # Wait for login to complete
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "form_kuisoner-p-0")))

    # Fill in the survey form
    # +------------------------------------------------------+
    # |  Feel free to adjust the range of the loop,          |
    # |  depending on the number of sections in the survey,  |
    # |  in this case, the survey has 10 sections            |
    # +------------------------------------------------------+
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
            try:
                radio_box = p_0_element.find_elements(By.CLASS_NAME, "pt-0")[2]
                radio_button = radio_box.find_element(By.TAG_NAME, "input")
                print("clicked" + radio_box.text)
                radio_button.click()
            except:
                print("error")

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
    time.sleep(5)
    # Close the browser after completing the task
    driver.quit()

