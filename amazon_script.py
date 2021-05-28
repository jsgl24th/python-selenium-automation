from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# init driver
driver = webdriver.Chrome(executable_path=r'C:\Users\jsglu\Automation\python-selenium-automation\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

# open the url
driver.get('https://www.amazon.com/')
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Table')
driver.find_element(By.ID, 'nav-search-submit-text').click()

actual_result = driver.find_element(By.XPATH,"//span[@class='a-color-state a-text-bold']").text
expected_result = '"Table"'
#print(actual_result)
#print(expected_result)

assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}'

driver.quit()
