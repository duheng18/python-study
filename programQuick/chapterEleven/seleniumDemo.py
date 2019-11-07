from selenium import webdriver

brower = webdriver.Firefox()
# <class 'selenium.webdriver.firefox.webdriver.WebDriver'>
print(type(brower))
brower.get('http://inventwithpython.com/')
