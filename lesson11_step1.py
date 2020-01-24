from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def func():
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
button = browser.find_element_by_id('book')
func()
button.click()
x = browser.find_element_by_id('input_value').text
ans = browser.find_element_by_id('answer')
ans.send_keys(calc(x))
submit_button = browser.find_element_by_id('solve')
submit_button.click()
time.sleep(10)
browser.quit()

