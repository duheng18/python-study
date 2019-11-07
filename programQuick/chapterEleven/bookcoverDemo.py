from selenium import webdriver

brower = webdriver.Firefox()
brower.get('http://inventwithpython.com')
try:
    elem = brower.find_element_by_class_name('pygame')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
