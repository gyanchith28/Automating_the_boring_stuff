from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')

element = browser.find_element_by_tag_name('html')

while True:
    element.send_keys(Keys.UP)
    element.send_keys(Keys.RIGHT)
    element.send_keys(Keys.DOWN)
    element.send_keys(Keys.LEFT)