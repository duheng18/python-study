from selenium import webdriver

browser = webdriver.Firefox()

# <class 'selenium.webdriver.firefox.webdriver.WebDriver'>
print(type(browser))

browser.get('http://inventwithpython.com/')
try:
    ele = browser.find_element_by_class_name('name')
    print('Found <%s> element with that class name!' % (ele.tag_name))
except:
    print('Was not able to find an element with that name.')

