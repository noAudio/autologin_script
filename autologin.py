from selenium import webdriver

browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
browser.get('https://www.google.com')