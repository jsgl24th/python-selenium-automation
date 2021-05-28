from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome(executable_path=r'C:\Users\jsglu\Automation\python-selenium-automation\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')
try:
    elements = driver.find_element(By.ID,'helpsearch')
    elements.send_keys('Cancel order:')
    elements.send_keys(Keys.RETURN)

    actual_res = driver.find_element(By.XPATH,"//b[contains(text(),'Cancel order')]").text
    expected_res = 'Cancel order:'

    assert expected_res == actual_res, f'Not equal {actual_res} to {expected_res}'
except AssertionError as msg:
    print(msg)
finally:
    driver.quit()
